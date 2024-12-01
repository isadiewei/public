#!/bin/bash

# this is a setup script for linux systems
# recommended to run using "sudo ./setup.sh"

# connecting to wifi while using ubuntu can be done using this password is optional 
# nmcli (d)evice wifi (c)onnect {hostname} password {password}
# e.g. nmcli d wifi c MyWifiName [password MyWifiPassword]

# update system and install python and a software package manager pip
sudo apt update
sudo apt upgrade
sudo apt install python3
sudo apt install python3-pip

# install python libraries using pip
sudo pip install pypdf
sudo pip install img2pdf

###
# EXECUTION INSTRUCTIONS EXAMPLE: python3 combine_images.py path_to_my_pdf_folder/
###
