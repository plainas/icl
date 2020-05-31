
# install icl python script on /usr/bin/icl
curl https://raw.githubusercontent.com/plainas/icl/master/icl.py --output icl
chmod +x icl
sudo mv icl /usr/bin/icl

mkdir -p ~/.config/icl/
curl https://raw.githubusercontent.com/plainas/icl/master/commands.txt --output ~/.config/icl/commands.txt

# configure zsh integration
curl https://raw.githubusercontent.com/plainas/icl/master/icl.zsh.sh >> ~/.zshrc