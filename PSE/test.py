import KEYPAD, time
import RFIDread as RFID
import char_lcd as LCD

#initialize lcd
lcd = LCD.init()
lcd.message('     Welcome')

def show_message(message):
    lcd.clear()
    lcd.message(message)

