import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
print('this is RFID')

def rfid_read():
    try:
        id, text = reader.read()
        print(id)
        print(text)
        
    finally:
        GPIO.cleanup()
        
def rfid_write():
    try:
        text = input('New Data:')
        print("now place your tag to write")
        reader.write(text)
        print("written")
    finally:
        GPIO.cleanup()

rfid_read()
    
