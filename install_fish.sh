#!/bin/sh

# install icl python script on /usr/bin/icl
mkdir -p ~/.config/icl/
curl https://address_to_snippersfile --output ~/.config/icl/commands.txt
curl http://address_to_icl.py --output icl
chmod +x icl
sudo mv icl /usr/bin/icl

# configure fish integration, you could pack this as a fisherman plugin instead, for example
mkdir -p ~/.config/fish/
curl https://address_to_fish >> ~/.config/fish/config.fish