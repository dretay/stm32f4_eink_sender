#! /usr/bin/python

import smbus2

bus = smbus2.SMBus(1)

DEVICE_ADDRESS = 0x03      #7 bit address (will be left shifted to add the read write bit)
DEVICE_REG_MODE1 = 0x00
DEVICE_REG_LEDOUT0 = 0x1d

#Write a single register
bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_MODE1, 0x80)

#Write an array of registers
# ledout_values = [0xff, 0xff, 0xff, 0xff, 0xff, 0xff]
# bus.write_i2c_block_data(DEVICE_ADDRESS, DEVICE_REG_LEDOUT0, ledout_values