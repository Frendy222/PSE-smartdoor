import RPi.GPIO as GPIO
import char_lcd as LCD
import time
from mfrc522 import SimpleMFRC522

#variable
cur = []
attempt = 0
message = '     Welcome'

#setup RFID for reading
reader = SimpleMFRC522()

#set up keypad
GPIO.setmode(GPIO.BCM) 
MATRIX = [
      [1,2,3,'A'],
      [4,5,6,'B'],
      [7,8,9,'C'],
      ['*',0,'#','D']
    ]

ROW = [5,6,13,19]
COL = [7, 1, 12, 16]

for j in range(4):
    GPIO.setup(COL[j], GPIO.OUT)
    GPIO.output(COL[j], 1)

for i in range(4):
    GPIO.setup(ROW[i],GPIO.IN, pull_up_down = GPIO.PUD_UP)


#setup lcd
lcd = LCD.init()
lcd.message(message)



#main
try:
    while True:
        
        for j in range(4):
            GPIO.output(COL[j],0)
                
            for i in range(4):
                if(GPIO.input(ROW[i])) == 0:
                    
                    #input data only 8 digit
                    input = MATRIX[i][j]
                    if len(cur) < 8:
                        cur.append(input)
                        print (cur)
                        lcd.clear()
                        message = 'Pass :'
                        lcd.message(message)
                        for k in range(len(cur)):
                            lcd.clear()
                            message += '*'
                            lcd.message(message)
                       
                    #if wrong input
                    else:
                        attempt += 1
                        print(attempt)
                        if attempt < 3:
                            del cur[:]
                            print(cur)
                            lcd.clear()
                            message = "  Please try it\n      again"
                            lcd.message(message)
                            time.sleep(2.0)
                            lcd.clear()
                            message = "Pass :"
                            lcd.message(message)
                            
                        else:
                            lcd.clear()
                            message = "Please try again \n   with RFID"
                            lcd.message(message)
                    while(GPIO.input(ROW[i]) == 0):
                        pass

            GPIO.output(COL[j],1)

except KeyboardInterrupt:
    GPIO.cleanup()
