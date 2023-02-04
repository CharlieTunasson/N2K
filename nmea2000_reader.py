import can
import time
from pynmea2 import parse

bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=500000)

while True:
    message = bus.recv()
    if message.arbitration_id == 0x0FEE:
        try:
            nmea_sentence = message.data.decode()
            data = parse(nmea_sentence)
            print(data)
        except:
            pass
    time.sleep(0.5)
