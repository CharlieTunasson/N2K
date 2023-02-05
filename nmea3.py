import can

# initialize the CAN bus
bus = can.interface.Bus(channel='can0', bustype='socketcan')

# listen to the incoming CAN messages
for msg in bus:
    print(msg)
