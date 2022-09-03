
#
# * Project: Nackademin
# * File: Dag1/python/step2.py
# * Author: Emil Nilsson
# * Contact: emil.nilsson@nutanix.com
#


# Imports
import serial
import requests
import json

ser = serial.Serial('/dev/tty.usbmodem14424101', 9600, timeout=1) # Connect to the Arduino serial connection


url = "http://10.0.0.177:8123/api/states/sensor.temp001" # Set URL for REST requests


# Set the header for the REST requests, API token from Home Assistant
headers = {
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI3MjQ5ZDRmNDMwNjI0ZTkxOWU3MTRkZmM2YmM3N2EzMyIsImlhdCI6MTU5ODg3OTI0OCwiZXhwIjoxOTE0MjM5MjQ4fQ.ZAXmTYD7xP-z0txBH-TVY5ju0CbByxp88wzpdvvpu7I'
}

# Run always
while True:

    value = ser.readline() # Read from the serial connection

    if(value): # IF there is data on the line

        # Construct payload for REST request
        payload = {
            "state": float(value), # Insert value from Arduino
            "attributes": {
                    "unit_of_measurement": "°C"
                }
            }

        response = requests.request("POST", url, headers=headers, data = json.dumps(payload)) # Do the REST request
        print(response.text.encode('utf8')) # Ourput the result of the REST request




