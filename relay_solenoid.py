import RPi.GPIO as GPIO
import time

# solenoidPin = 21
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(solenoidPin, GPIO.OUT)
# GPIO.output(solenoidPin, GPIO.LOW)
# GPIO.setwarnings(False)

def unlock(solenoidPin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(solenoidPin, GPIO.IN)
    GPIO.setwarnings(False)
    
    GPIO.setup(solenoidPin, GPIO.OUT)
    print("ACCESS GRANTED")
    time.sleep(4)
    GPIO.setup(solenoidPin, GPIO.IN)

# user = "sherlyn"
# check(user)
# unlock()
# GPIO.cleanup()

if __name__ == '__main__':
    pass
