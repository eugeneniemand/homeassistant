# Enable SSH 

# set static IP
interface eth0
static ip_address=192.168.1.3/24
static routers=192.168.1.1
static domain_name_servers=192.168.1.1 8.8.8.8 

passwd
apt update
apt ugrade
#install docker
## stretch
curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh

## buster
sudo apt-get install docker.io docker-compose

sudo apt-get install docker-ce=18.06.1~ce~3-0~raspbian
sudo usermod -aG docker pi
sudo groupadd docker
sudo gpasswd -a $USER docker
sudo systemctl enable docker.service
sudo reboot
sudo apt install git -y
sudo apt-get install -y python-cffi
sudo apt-get install -y python python-pip 
sudo pip install docker-compose

ssh-keygen
git clone git@github.com:eugeneniemand/homeassistant.git

# Symlink the service file to the correct location
sudo ln -s /home/pi/homeassistant/ha.service /etc/systemd/system/ha.service

docker-compose up -d
<!-- docker run --name="mqtt" -dtp 1883:1883 -p 9001:9001 pascaldevink/rpi-mosquitto
docker run --name="zigbee2mqtt" -d -v /home/pi/data:/app/data --device=/dev/ttyACM0 koenkk/zigbee2mqtt:arm32v6
docker run --name="home-assistant" --init -d -v /home/pi/homeassistant:/config -v /etc/localtime:/etc/localtime:ro --net=host homeassistant/raspberrypi3-homeassistant 
docker run -d \
--name=ha-dockermon --restart=always \
-v /var/run/docker.sock:/var/run/docker.sock \
-v /path/to/config:/config \
-p 8126:8126 \ 
philhawthorne/ha-dockermon -->