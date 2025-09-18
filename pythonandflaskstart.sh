#!/bin/bash

#package update
sudo apt update
#all for flask
sudo apt install python3 python3-pip python3-venv
#create project in home directory
cd ~ 

mkdir firstproject flask && cd firstproject/

#create and activate venv
python3 -m venv firstvenv && source ~/firstproject/firstvenv/bin/activate
#install flask
pip install flask
#show flask version
pip show flask