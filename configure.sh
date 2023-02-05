#!/bin/bash

# Install python3 and pip
sudo apt-get update
sudo apt-get install -y python3 python3-pip

# Install the python-can library
sudo pip3 install python-can

# Create a virtual CAN interface
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0

# Run the python script that reads data from the NMEA 2000 network
python3 nmea2000_read.py
