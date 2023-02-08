# import can

# # initialize the CAN bus
# bus = can.interface.Bus(channel='can0', bustype='socketcan')

# # listen to the incoming CAN messages
# for msg in bus:
#     print(msg)

import can

# Initialize the CAN bus using the "socketcan" interface
bus = can.Bus(channel='can0', bustype='socketcan')

# Continuously listen for incoming messages on the CAN bus
while True:
    message = bus.recv()
    if message is not None:
        # Print the message data
        print("ID: 0x{:03X} Data: {}".format(message.arbitration_id, message.data))
