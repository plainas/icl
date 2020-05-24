
# install icl python script on /usr/bin/icl
curl https://raw.githubusercontent.com/plainas/icl/master/icl.py --output icl
chmod +x icl
sudo mv icl /usr/bin/icl

mkdir -p ~/.config/icl/
curl https://raw.githubusercontent.com/plainas/icl/master/commands.txt --output ~/.config/icl/commands.txt

# configure fish integration, you could pack this as a fisherman plugin instead, for example
mkdir -p ~/.config/fish/
curl https://raw.githubusercontent.com/plainas/icl/master/icl.fish >> ~/.config/fish/config.fish