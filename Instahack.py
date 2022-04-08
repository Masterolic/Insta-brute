clear
echo -e '\e[92m
               ╦╔═╗  ╦ ╦╔═╗╔═╗╦╔═
               ║║ ╦──╠═╣╠═╣║  ╠╩╗
               ╩╚═╝  ╩ ╩╩ ╩╚═╝╩ ╩'  
apt install -y python2 python tor wget
pip install --upgrade pip
pip install requests
pip install stem

echo -e "\e[34mSETTING UP SERVERS.....WAIT\e[0m"
cd $HOME >/dev/null 2>&1
wget -O ~/instapy-config.json "https://git.io/v5DGy" >/dev/null 2>&1
