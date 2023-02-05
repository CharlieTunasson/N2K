#!/bin/bash

# Install necessary packages
sudo apt-get update
sudo apt-get install python3-pip can-utils python3-smbus

# Create a virtual CAN interface
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0

