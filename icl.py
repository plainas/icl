#!/usr/bin/env python

import contextlib
import curses
import io
import os
import signal
import sys
import threading
import time
#uuuh.... if I remove this, curses.ascii is not found!?!??! WTF?
from curses.textpad import Textbox, rectangle
import pathlib


# ==============================================================================
# taken from https://github.com/mooz/percol
# ==============================================================================

def get_ttyname():
    for f in sys.stdin, sys.stdout, sys.stderr:
        if f.isatty():
            return os.ttyname(f.fileno())


def reconnect_descriptors(tty):

    # all this tricky stuff is needed because python curses binding doesn't have a binding for newterm()
    # But this could be solved if other language is used istead od python
    # https://stackoverflow.com/questions/8371877/ncurses-and-linux-pipeline

    target = {}

    stdios = (("stdin", "r"), ("stdout", "w"), ("stderr", "w"))

    tty_desc = tty.fileno()

    for name, mode in stdios:
        f = getattr(sys, name)

        if f.isatty():
            # f is TTY
            target[name] = f
        else:
            # f is other process's output / input or a file

            # save descriptor connected with other process
            std_desc = f.fileno()
            other_desc = os.dup(std_desc)

            # set std descriptor. std_desc become invalid.
            os.dup2(tty_desc, std_desc)

            # set file object connected to other_desc to corresponding one of sys.{stdin, stdout, stderr}
            try:
                target[name] = os.fdopen(other_desc, mode)
                setattr(sys, name, target[name])
            except OSError:
                # maybe mode specification is invalid or /dev/null is specified (?)
                target[name] = None
                print("Failed to open {0}".format(other_desc))

    return target


# ==============================================================================
# End of percol code
# ==============================================================================


def get_entries_from_file():

    commands_file_path = pathlib.Path.home() / ".config" / "icl" / "commands.txt"

    if not commands_file_path.is_file():
        sys.exit("Error!!! Commmands file is missing. Trying to read from: " + str(commands_file_path))

    f = open(commands_file_path, "r")
    all_file_lines = [line.rstrip('\n') for line in f]
    f.close()

    entries = []
    saved_entry_name = None
    processing_en_entry = False
    for line in all_file_lines:
        if len(line) > 0 and line[0] == '#':
            saved_entry_name = line
            processing_en_entry = True
            continue
        if processing_en_entry:
            entries.append((saved_entry_name, line))
            processing_en_entry = False
    return entries



class Icl():
    def __init__(self):
        self.input_string=""
        self.all_entries = get_entries_from_file()
        self.matches = []
        self.selected_option_index = 0
        
        self.screen = curses.initscr()
        self.screen.clear()
        # signal.signal(signal.SIGINT, lambda signum, frame: None)
        self.screen.keypad(True)
        curses.raw()
        curses.noecho()
        curses.cbreak()
        curses.nonl()
        
        curses.start_color()
        curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_MAGENTA)
        curses.newwin(0,0)
        self.screen.keypad(1)
        self.screen.addstr(0,0, "QUERY>")

        try:
            self.process_new_input()
            while True:
                pressed_key = self.screen.getch()
                self._handle_keypress(pressed_key)
                self.process_new_input()
        except:
            #TODO: maybe catch only keyboard interrupt????
            curses.nocbreak()
            self.screen.keypad(False)
            curses.echo()
            curses.nl()
            curses.endwin()
            # raise


    def _get_vertical_real_estate(self):
        """
        How many snippets fit in the screen?
        """
        screen_height, _ = self.screen.getmaxyx()
        return (screen_height - 1) // 2



    def _match(self, entry, query):
        query_words = query.split()

        for word in query_words:
            if word not in entry[0] and word not in entry[1]:
                return False
        return True


    def _search_suggestions(self, query_string):
        del self.matches[:]
        [self.matches.append(e) for e in self.all_entries if self._match(e, query_string)]
        self.screen.move(1,0)

        # erase from cursor to end of window
        self.screen.clrtobot()

        screen_vertical_real_estate = self._get_vertical_real_estate()

        for idx, match in enumerate(self.matches[:screen_vertical_real_estate]):
            try:
                line_number = idx * 2 + 1
                if self.selected_option_index != idx:
                    self.screen.addstr(line_number, 0, match[0] ,curses.color_pair(1) | curses.A_BOLD)
                    self.screen.addstr( line_number +1 , 0, match[1])
                else:
                    self.screen.addstr(line_number, 0, match[0] ,curses.color_pair(2) | curses.A_BOLD)
                    self.screen.addstr( line_number +1 , 0, match[1], curses.color_pair(2))

                self.screen.move(0 , 7+ len(query_string))
            except:
                exit(match)


    def process_new_input(self):
        self.screen.move(0,7)
        self.screen.clrtoeol()
        self.screen.addstr(self.input_string)
        self.screen.refresh()
        self._search_suggestions(self.input_string)


    def _handle_keypress(self, pressed_key):

        if pressed_key == 8 or pressed_key == 127 or pressed_key == curses.KEY_BACKSPACE:
            self.input_string = self.input_string[:-1]

        elif pressed_key == curses.KEY_ENTER or pressed_key == 10 or pressed_key == 13:
            final_output=self.matches[self.selected_option_index][1]
            curses.nocbreak()
            self.screen.keypad(False)
            curses.echo()
            curses.nl()
            curses.endwin()
            sys.stdout.flush()
            sys.stdout.buffer.write(final_output.encode('utf-8'))
            sys.stdout.buffer.write(b"\n")
            sys.stdout.flush()
            sys.exit()

        elif pressed_key == curses.KEY_DOWN:
            screen_vertical_real_estate = self._get_vertical_real_estate()
            if self.selected_option_index < screen_vertical_real_estate - 1:
                self.selected_option_index += 1

        elif pressed_key == curses.KEY_UP:
            if self.selected_option_index > 0:
                self.selected_option_index -= 1

        elif curses.ascii.isprint(pressed_key): # this also needs to be replaced by something.
            x,y = curses.getsyx()
            self.input_string  = self.input_string + str(chr(pressed_key))
            self.selected_option_index = 0



ttyname =  get_ttyname()

with open(ttyname, "wb+", buffering=0) as tty_f:
    reconnect_descriptors(tty_f)
    Icl()
