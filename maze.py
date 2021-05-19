import time
import FA

fa = FA.Create()
fa.ComOpen(6)

fa.LCDClear()

clear = 100
wall = 20

while True:
    leftSensor = fa.ReadIR (0)
    frontSensor = fa.ReadIR (2)
   

    if leftSensor < 50 and frontSensor < 50:
        fa.Forwards(10)
        print(frontSensor, leftSensor)
        #time.sleep(1)

    elif frontSensor > 50:
        fa.Right(90)

    #elif leftSensor < 20:
        #fa.Forwards(0)
       # fa.leftSensor(90)

    #elif front > 50:
        #fa.Forwards(0)
       # fa.Right(90)

   # elif leftSensor <= wall and front <= wall:
        #fa.Forwards(0)
        #fa.Right(90)

fa.ComClose()
