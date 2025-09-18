#!/bin/bash

#install OPENSSH server
sudo apt-get install -y openssh-server

#install net-tools and policycoreutils
sudo apt-get install -y net-tools policycoreutils

#check SELinux status
sestatus

#systemctl status ssh 
sudo systemctl status ssh

sudo systemctl start ssh
#found ready ssh keys
ls -al ~/.ssh/id_*.pub
#create ssh keys
if [ $? -ne 0 ]; then
    echo "SSH key pair not found. Generating a new keys"
    echo "Enter your email address for the SSH key:"
    read EMAIL
    ssh-keygen -t rsa -b 4096 -C "$EMAIL"
else
    echo "SSH key pair found."
fi

ls -al ~/.ssh/id_*pub

#rewrite the key in authorized_keys
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys


cd ~


 