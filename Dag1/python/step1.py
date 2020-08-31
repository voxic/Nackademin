
#
# * Project: Nackademin
# * File: Dag1/python/step1.py
# * Author: Emil Nilsson
# * Contact: emil.nilsson@nutanix.com
#

# Imports
import serial

ser = serial.Serial('/dev/tty.usbmodem14421101', 9600, timeout=1) # Connect to the Arduino serial connection

# Run always
while True:

    value = ser.readline() # Read from the serial connection

    if(value): # IF there is data on the line
        print(float(value)) # Convert string to float and output the data from Arduino
