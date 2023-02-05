#!/bin/bash

# Install necessary packages
sudo apt-get update
sudo apt-get install -y python3-pip python3-can can-utils

# Create a virtual CAN interface
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set vcan0 up

# Start the Python script to read NMEA 2000 data from the compass sensor
python3 -u read_compass.py vcan0
