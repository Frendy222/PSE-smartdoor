import RPi.GPIO as GPIO
import time

solenoidPin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(solenoidPin, GPIO.OUT)
GPIO.output(solenoidPin, GPIO.LOW)
GPIO.setwarnings(False)

def check(result):
    while True:  
            
        if(result == 'sherlyn'):
            GPIO.output(solenoidPin, GPIO.LOW)
            print("ACCESS GRANTED")
            time.sleep(2)
            GPIO.output(solenoidPin, GPIO.HIGH)
        else:
            print("ACCESS DENIED")
        break

# check('sherlyn')