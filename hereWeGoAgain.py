import socketcan
import can
import PyNMEA2

can_interface = 'can0'
bus = can.interface.Bus(can_interface, bustype='socketcan_native')

for msg in bus:
    if msg.arbitration_id == PyNMEA2.PRIVATE_ISOTP_ID:
        try:
            sentence = PyNMEA2.parse(msg.data)
            print(sentence)
        except PyNMEA2.ParseError as error:
            print("Parse error:", error)