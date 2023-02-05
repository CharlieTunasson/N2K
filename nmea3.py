import can

# Set up the CAN bus interface
bus = can.interface.Bus(channel='vcan0', bustype='socketcan_native')

# Continuously read data from the NMEA 2000 network
while True:
    message = bus.recv()
    print(message)
