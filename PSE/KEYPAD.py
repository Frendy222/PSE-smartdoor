import RPi.GPIO as GPIO
import char_lcd as LCD
import RFIDread as RFID
import relay_solenoid as RELAY

#initialize lcd
lcd = LCD.init()
lcd.message('     Welcome')

def show_message(message):
    lcd.clear()
    lcd.message(message)

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
    
    GPIO.setmode(GPIO.BCM) 

    for j in range(4):
        GPIO.setup(COL[j], GPIO.OUT)
        GPIO.output(COL[j], 1)

    for i in range(4):
        GPIO.setup(ROW[i],GPIO.IN, pull_up_down = GPIO.PUD_UP)

def limit_input(limit):
    keypad_init()
    matrix = matrix_data()
    row = row_data()
    col = col_data()
    
    password = []
    message = 'pass :'
    
    try:
        while limit != 0:
            for j in range(4):
                GPIO.output(col[j],0)
                    
                for i in range(4):
                    if(GPIO.input(row[i])) == 0:
                        pin = matrix[i][j]
                        if pin == 'D':
                            show_message('    RFID MODE')
                            user = RFID.read()
                            RELAY.check(user)
                            return user
                        password.append(pin)
                        limit -= 1
                        message += '*'
                        show_message(message)
#                         print ('Password :' + str(password))
#                         print ('limit    :' + str(limit))
                        while(GPIO.input(row[i]) == 0):
                            pass

                GPIO.output(col[j],1)

    except KeyboardInterrupt:
        GPIO.cleanup()
    
    return password

def main():
    keypad_init()
    matrix = matrix_data()
    col = col_data()
    row = row_data()
    try:
        while True:
            for j in range(4):
                GPIO.output(col[j],0)
                    
                for i in range(4):
                    if(GPIO.input(row[i])) == 0:
                        print (matrix[i][j])
                        while(GPIO.input(row[i]) == 0):
                            pass

                GPIO.output(col[j],1)

    except KeyboardInterrupt:
        GPIO.cleanup()        
print(limit_input(5))
# RFID.read()
# RFID.write()