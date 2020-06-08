# icl - interactive command library

`icl` is a user-friendly, interactive cheat sheet for your UNIX terminal.

Have your favorite one-liners allways at your fingertips.

![Example](./screencast.svg)

## Installation

One line installation is provided for convenience, but you are encouraged to read the installation scripts.

### Fish shell

```shellscript
curl -sSL https://raw.githubusercontent.com/plainas/icl/master/install_fish.sh | /bin/sh
```

Reload your fish config or start a new shell.

Note:
Iy you are still using fish 2, yon need to define the keybinding to ''f_run_icl'' yourself.


### Z shell

```shellscript
curl -sSL https://raw.githubusercontent.com/plainas/icl/master/install_zsh.sh | /bin/sh
```

reload zsh config or relaunch zsh.

### Bash


```shellscript
curl -sSL https://raw.githubusercontent.com/plainas/icl/master/install_bash.sh | /bin/sh
```

Bash doesn't lend itself to the same level of interactivity and configurability as fish or zsh.

The command below will install a function to launch `icl` by pressing `Ctrl+t`, on your `.bashrc` .
The chosen command is placed in your input bugger but it is also printed to stdout. This works but
it is somewhat anoying. If you are bash user, this is good time to switch to fish.


### Manual Installation

`icl` command is just a single python script with no dependencies on third party modules. By itself, it just launches the interactive search UI and, once you pick a command by pressing enter, will send it to SDOUT. This is not too useful. For a streamlined experience, install the helper functions for your shell and bind them to shortcut. They will launch icl on a keybind and, once you pick the command, place it in your input buffer. Check `icl.fish`, `icl.bash.sh` and `icl.zsh.sh` for ready to use helper functions and keybinding definitions.

1. Download `icl.py`, set the execution bit and place it somewhere on your `$PATH`.

2. Install the helper functions and keybinds for your shell.

## Usage

Just press `Ctrl+t` and start typing.

Pick the command you want by pressing enter. To abort press `Ctrl+C`

## A commands to your cheat sheet

Commmands are stored in `~/.config/icl/commands.txt`

You can edit that file and add your favorite oneliners.

The format is self explanatory:

```shellscript

# description lines starts with '#', the command follows in the next line
fortune

# This line is here just to hold a brief command description
echo "This sample command echoes this!" 

# List all processes
ps aux

```

### Bonus: icl as a [TLDR](https://tldr.sh/) client

The file `tldr.txt` includes all commands scrapped from tldr repository. If you want to be able to access them using icl, simply place them in your `commands.txt`. You can do so by running the following command.

```
curl https://raw.githubusercontent.com/plainas/icl/master/tldr.txt >> ~/.config/icl/commands.txt
```

### TODO
* accept an url as parameter to load an online library
* include  and [cheat](https://github.com/cheat/cheat) [eg](https://github.com/srsudar/eg)
* integrate client to [bropages](http://bropages.org/)
* Improve TLDR scraper, get ridd of curly brackets around paremeters.
