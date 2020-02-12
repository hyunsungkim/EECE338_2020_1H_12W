#!/bin/bash

# Install essential linux packages
sudo apt-get install -y python-pip ibus fonts-unfonts-core vim
python3 -m pip install numpy 

# Install scipy and matplotlib library manually
cd ..
mkdir temp_ & cd temp_
sudo wget https://www.piwheels.org/simple/scipy/scipy-1.3.3-cp37-cp37m-linux_armv7l.whl#sha256=edda366fda13cfad10c3cf58341297f0ff1255020076a247ce50e594b42849d0
sudo wget https://www.piwheels.org/simple/matplotlib/matplotlib-3.2.0rc1-cp37-cp37m-linux_armv7l.whl#sha256=0d277848deff8ae2b31eaad3c8a7d65fd9b2dc5d8cb89d36346813d63a57f286
sudo pip3 install scipy-1.3.3-cp37-cp37m-linux_armv7l.whl
sudo pip3 install matplotlib-3.2.0rc1-cp37-cp37m-linux_armv7l.whl
cd .. & sudo rm -rf temp_  

# Install required linux packages and python libraries
cd ~/POSTECH_EE_EXP2
sudo chmod +x ./scripts/*
./scripts/*.sh
