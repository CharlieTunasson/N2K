#!/bin/bash

# update the package list
sudo apt-get update

# install the python3 pip package manager
sudo apt-get install -y python3-pip

# install the python CAN library
pip3 install python-can

# install the socketCAN utilities
sudo apt-get install -y can-utils
