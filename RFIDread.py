import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

def read_tag():
    print ('rfid mode')
    reader = SimpleMFRC522()
    try:
        id, text = reader.read()
        text.strip()
        print('id   :' + str(id))
        print('User :' + text)
    except:
        print("error")
    finally:
#         GPIO.cleanup()
        pass
    return text
    
def write_tag():
    reader = SimpleMFRC522()
    try:
        text = input('New Data:')
        print("now place your tag to write")
        reader.write(text)
        print("written")
    finally:
#         GPIO.cleanup()
        pass
# GPIO.cleanup()
# write()
if __name__ == "__main__":
    read_tag()