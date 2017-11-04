# coding: utf-8
import smbus
import time

# use ic2 bus 2
bus = smbus.SMBus(2)
    
   
for cycle in range(100):
    # write 0x51 to register 0x00 of a device located at 0x70 on this bus.
    bus.write_byte_data(0x70,0x00,0x51)
    time.sleep(67e-03)  # wait 67ms
    #print(bus.read_byte_data(0x70,0x02)) # Not sure yet what this value means.
    print('The distance is ' + str(bus.read_byte_data(0x70,0x03)) + ' cm')
