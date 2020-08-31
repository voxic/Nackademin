# Introduktion till Internet of Things

## Arduino till Home Assistant

### 1. Skapa "Long-Lived Access Token" i Home Assistant

1. Öppna Home Assistant och klicka på din profil i det nedre vänstra hörnet.
2. Längst ned på sidan hittar du "Long-Lived Access Token", skapa en och kopiera strängen till en fil.

### 2. Installation Python moduler

Använd PIP3 för att installera de python moduler vi kommer att behöva för att skriva en brygga mellan Arduino och Home Assistant.

Öppna en terminal och skriv in:

```bash
pip3 install requests
pip3 install pyserial
```

### 3. Python program

Öppna en ny tom fil i kodeditor.

Börja med följande program:

```python
# Imports
import serial

ser = serial.Serial('/dev/tty.usbmodem14421101', 9600, timeout=1) # Connect to the Arduino serial connection

# Run always
while True:

    value = ser.readline() # Read from the serial connection

    if(value): # IF there is data on the line
        print(float(value)) # Convert string to float and output the data from Arduino
```

Source: https://github.com/voxic/Nackademin/blob/master/Dag1/python/step1.py

> **TIPS!** För att ta reda på vilken COM/port som arduino är ansluten till, kolla i Arduino IDE

När du kör detta program borde du se temperaturvärden komma från din Arduino.

```bash
22.27
21.78
22.27
22.27
```

### 4. Skicka data till Home Assistant

I detta steg ska vi använda oss av "Long-Lived Access Token" för att autentisera oss och skicka data till Home Assistant.

Gör en kopia av ditt första Python program och utöka det enligt följande:

```python
# Imports
import serial
import requests
import json

ser = serial.Serial('/dev/tty.usbmodem14424101', 9600, timeout=1) # Connect to the Arduino serial connection


url = "http://10.0.0.177:8123/api/states/sensor.temp001" # Set URL for REST requests


# Set the header for the REST requests, API token from Home Assistant
headers = {
  'Authorization': 'Bearer DIN Long-Lived Access Token HÄR'
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
```

Var noga med att använda **DIN** COM/port till Arduino och **DIN** IP till Home Assistant

> **TIPS!** IP till Home Assistant tog vi fram i Lab 01-1

> **TIPS!** Du kan byta ut sensor.temp001 till ett eget namn.

När du kör detta program bör du se en konfirmation på att data skickats till Home Assistant i terminalen

```bash
b'{"attributes": {"unit_of_measurement": "\\u00b0C"}, "context": {"id": "5f178db5eba611eaad5e17231ec424c9", "parent_id": null, "user_id": "5867b27318cc4b19a4d2b7f8725a42c9"}, "entity_id": "sensor.temp001", "last_changed": "2020-08-31T16:23:58.069946+00:00", "last_updated": "2020-08-31T16:23:58.069946+00:00", "state": "20.8"}'
```

Din sensor bör även dyka upp på första sidan i Home Assistant.