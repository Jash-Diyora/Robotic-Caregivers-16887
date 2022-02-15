#Turn On: A0 01 01 A2
#Turn Off: A0 01 00 A1
#Python example code:
#link1: https://www.smart-prototyping.com/USB-Relay-1-Channel
#link2: https://www.amazon.com/Taidda-Durable-Lightweight-Intelligent-Control/dp/B07WFVN1FK/ref=sr_1_31?keywords=usb+relay&qid=1643605294&sr=8-31

import serial
import time

usb_relay = serial.Serial("COM17",9600)

if usb_relay.is_open:

   print(usb_relay)

   on_cmd = b'\xA0\x01\x01\xa2'

   off_cmd =  b'\xA0\x01\x00\xa1'

   usb_relay.write(on_cmd )

   time.sleep(1)

   usb_relay.write(off_cmd)

   time.sleep(1)

usb_relay.close()
