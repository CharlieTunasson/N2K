import can
import time

def read_compass(bus):
    # Check for messages on the CAN bus
    while True:
        message = bus.recv()
        if message.arbitration_id == 0x0CFF10:
            # This is the expected message from the compass sensor
            heading = (message.data[0] << 8 | message.data[1]) / 10
            print("Heading: {} degrees".format(heading))

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: {} <CAN interface>".format(sys.argv[0]))
        sys.exit(1)

    # Open the specified CAN interface
    bus = can.interface.Bus(channel=sys.argv[1], bustype='socketcan_ctypes')

    # Read compass data
    read_compass(bus)
