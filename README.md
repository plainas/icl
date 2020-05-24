# icl - interactive command library

icl is a user-friendly, interactive cheat sheet for your UNIX terminal.

Have your favorite one-liners allways at your fingertips.

## installation

One line installation is provided for convenience, but I encourage you read the
installation scripts.

### fish shell

This will only work for fish 3. If you use fish 2, you need to setup the keybind yourself

Todo: put these in files and install with pipe to shell interactive

/bin/sh -c "$(curl -sSL https://get.docker.com/)"


```shellscript
# install icl python script on /usr/bin/icl
mkdir -p ~/.config/icl/
curl https://address_to_snippersfile --output ~/.config/icl/commands.txt
curl http://address_to_icl.py --output icl
chmod +x icl
sudo mv icl /usr/bin/icl

# configure fish integration, you could pack this as a fisherman plugin instead, for example
mkdir -p ~/.config/fish/
curl https://address_to_fish >> ~/.config/fish/config.fish
```

### zshel

### bash

## usage

Just press Ctrl+t!

## adding commands to your cheat sheet

Commmands are stored in .config/icl/commands.txt

TODO: describe the format
TODO: mention tldr
TODO: add tldr scraiping script
TODO: mention how to install on fish 2

