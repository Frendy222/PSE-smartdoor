import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM) 
MATRIX = [
      [1,2,3,'A'],
      [4,5,6,'B'],
      [7,8,9,'C'],
      ['*',0,'#','D']
    ]

# COL = [17, 15,14,4]
# ROW = [5, 3, 27, 20]

ROW = [5,6,13,19]
COL = [7, 1, 12, 16]

for j in range(4):
    GPIO.setup(COL[j], GPIO.OUT)
    GPIO.output(COL[j], 1)

for i in range(4):
    GPIO.setup(ROW[i],GPIO.IN, pull_up_down = GPIO.PUD_UP)


try:
    while True:
        for j in range(4):
            GPIO.output(COL[j],0)
                
            for i in range(4):
                if(GPIO.input(ROW[i])) == 0:
                    print (MATRIX[i][j])
                    while(GPIO.input(ROW[i]) == 0):
                        pass

            GPIO.output(COL[j],1)

except KeyboardInterrupt:
    GPIO.cleanup()
