import smbus
import time

bus = smbus.SMBus(1)
address = 0x42

while True:
    data = bus.read_i2c_block_data(address, 0x00, 6)
    x = (data[0] << 8) | data[1]
    if x > 32767:
        x = x - 65536
    y = (data[2] << 8) | data[3]
    if y > 32767:
        y = y - 65536
    z = (data[4] << 8) | data[5]
    if z > 32767:
        z = z - 65536

    print("X: %d, Y: %d, Z: %d" % (x, y, z))
    time.sleep(1)
