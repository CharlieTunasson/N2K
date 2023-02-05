import can

def receive_messages():
    # Initialize the bus object
    bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
    
    # Infinite loop to receive messages
    while True:
        message = bus.recv()
        print("ID: ", message.arbitration_id)
        print("Data: ", message.data)
        print("Timestamp: ", message.timestamp)

# Call the receive_messages function
if __name__ == "__main__":
    receive_messages()