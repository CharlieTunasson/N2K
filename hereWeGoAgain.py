# import can

# # Initialize the CAN bus using the "socketcan" interface
# bus = can.Bus(channel='can0', bustype='socketcan')

# # Continuously listen for incoming messages on the CAN bus
# while True:
#     message = bus.recv()
#     if message is not None:
#         # Print the message data
#         print("ID: 0x{:03X} Data: {}".format(message.arbitration_id, message.data))

import can

# Initialize the CAN bus using the "socketcan" interface
bus = can.Bus(channel='can0', bustype='socketcan')

# Continuously listen for incoming messages on the CAN bus
while True:
    message = bus.recv()
    if message is not None:
        # Print the message data
        print("ID: 0x{:03X} Data: {}".format(message.arbitration_id, message.data))
