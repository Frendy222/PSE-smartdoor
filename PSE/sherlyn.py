import firebase
import firebase_admin
from firebase_admin import credentials
import RPi.GPIO as GPIO
import time

#cred = credentials.Certificate("path/to/serviceAccountKey.json")
#irebase_admin.initialize_app(cred)
firebase = firebase.FirebaseApplication('https://pse-smartdoor.firebaseio.com')

result = firebase.get('/smartdoor/access_history/name', None)
print(result)


# Configure Variables


# Configure GPIO
solenoidPin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(solenoidPin, GPIO.OUT)
GPIO.output(solenoidPin, GPIO.LOW)
GPIO.setwarnings(False)

while(1):  
        
    if(result == 'sherlyn'):
        GPIO.output(solenoidPin, GPIO.LOW)
        print("ACCESS GRANTED")
        time.sleep(2)
        GPIO.output(solenoidPin, GPIO.HIGH)
    else:
        print("ACCESS DENIED")
    break
