#!/usr/bin/env bash
# sets up the web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "hello world" | sudo tee /data/web_static/releases/test/index.html

target="/data/web_static/releases/test/"
symlink="/data/web_static/current"
if [ -e "$symlink" ]; then
    rm "$symlink"
fi
ln -s "$target" "$symlink"
sudo chown -R ubuntu:ubuntu /data/
sed -i "61i\ \n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t\tautoindex off;\n\t}" /etc/nginx/sites-available/default
sudo service nginx restart

