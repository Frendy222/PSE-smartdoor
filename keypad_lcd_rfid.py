import RPi.GPIO as GPIO
import char_lcd as LCD
import RFIDread as RFID
import relay_solenoid as RELAY
import firestore_data as STORE
import time

# GPIO.setmode(GPIO.BCM)
# #initialize lcd
# lcd = LCD.init()
# lcd.message('     Welcome')
# Global Variables
solenoidPin = 21

#to convert list of int into string
def convert(list): 
    res = int("".join(map(str, list))) 
    return res 

# def show_message(message):
# #     lcd.init()
#     lcd.clear()
#     lcd.message(message)
#     return lcd

def matrix_data():
    matrix = [
          [1,2,3,'A'],
          [4,5,6,'B'],
          [7,8,9,'C'],
          ['*',0,'#','D']
        ]
    return matrix

def row_data():
    row = [5,6,13,19]
    return row

def col_data():
    col = [7, 1, 12, 16]
    return col

def keypad_init():
    ROW = row_data()
    COL = col_data() 

    for j in range(4):
        GPIO.setup(COL[j], GPIO.OUT)
        GPIO.output(COL[j], 1)

    for i in range(4):
        GPIO.setup(ROW[i],GPIO.IN, pull_up_down = GPIO.PUD_UP)

def limit_input(limit):
    GPIO.setmode(GPIO.BCM)
    #initialize lcd
    lcd = LCD.init()
    lcd.message('     Welcome')
    
    keypad_init()
    matrix = matrix_data()
    row = row_data()
    col = col_data()
    
    password = []
    message = 'pass :'
#     print(str(password))
    #try:
    while limit != 0:
        for j in range(4):
            GPIO.output(col[j],0)
                
            for i in range(4):
                if(GPIO.input(row[i])) == 0:
                    pin = matrix[i][j]
                    if pin == 'D':
                        lcd.clear()
                        lcd.message('    RFID MODE')
                        user = RFID.read_tag()
                        RELAY.unlock(solenoidPin)
                        STORE.add_history("RFID Tag")
                        return user
                    password.append(pin)
                    limit -= 1
                    message += '*'
                    lcd.clear()
                    lcd.message(message)
                    while(GPIO.input(row[i]) == 0):
                        pass
                    
            GPIO.output(col[j],1)
                
                
    #except KeyboardInterrupt:
       # GPIO.cleanup()
    #if Pin input is right unlock
    if STORE.get_password() == str(convert(password)):
        lcd.clear()
        lcd.message(' Unlocked')
        RELAY.unlock(solenoidPin)
        STORE.add_history("Pin")
        lcd.clear()
        lcd.message(' Welcome ')
        
    if STORE.get_password() != str(convert(password)):
        lcd.clear()
        lcd.message(' Wrong Password')
        
    
    return password      

while True: print(limit_input(8))
# print(limit_input(8))

GPIO.cleanup()
