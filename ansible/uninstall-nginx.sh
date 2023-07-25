#!/bin/bash

# Color
GREEN='\033[0;32m'
NC='\033[0m' # No Color

echo -e "${GREEN}delete nginx ...${NC}"
apt-get remove nginx nginx-common -y
apt-get purge nginx nginx-common -y
apt-get autoremove -y

echo -e "${GREEN}delete docker...${NC}"
sudo apt-get purge -y docker-engine docker docker.io docker-ce  
sudo apt-get autoremove -y --purge docker-engine docker docker.io docker-ce  
sudo umount /var/lib/docker/
sudo rm -rf /var/lib/docker /etc/docker
sudo rm /etc/apparmor.d/docker
sudo groupdel docker
sudo rm -rf /var/run/docker.sock
sudo rm -rf /usr/bin/docker-compose

echo -e "${GREEN}install nginx ...${NC}"
apt update
apt install nginx -y

echo -e "${GREEN}install docker ....${NC}"
apt-get remove docker docker-engine docker.io containerd runc
apt-get update
apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release
rm -rf /usr/share/keyrings/docker-archive-keyring.gpg
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list >/dev/null
apt-get update
apt-get install -y docker-ce docker-ce-cli containerd.io
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
rm /usr/bin/docker-compose
ln -s /usr/local/bin/docker-compose /usr/bin/docker-composes

echo -e "${GREEN}change nginx webpage ...${NC}"
sed -i 's/Welcome to nginx!/Welcome to Chabokan!/g' /var/www/html/index.nginx-debian.html

echo -e "${GREEN}pull config ...${NC}"
git clone "https://github.com/mohammad76/config-server.git"

