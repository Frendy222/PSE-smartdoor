import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time

def read():
    print ('rfid mode')
    reader = SimpleMFRC522()
    try:
        id, text = reader.read()
        print('id   :' + str(id))
        print('User :' + text)
        
    finally:
        GPIO.cleanup()
    return text
    
def write():
    reader = SimpleMFRC522()
    try:
        text = input('New Data:')
        print("now place your tag to write")
        reader.write(text)
        print("written")
    finally:
        GPIO.cleanup()

# write()
# read()