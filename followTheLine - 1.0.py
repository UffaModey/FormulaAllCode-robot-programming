import time
import FA

fa = FA.Create()
fa.ComOpen(6)

fa.LCDClear()

white = 200 #Reflection value from a white surface
correction = 10 #correction angle
clapSound = 3000 #clap treshold to trigger motion of the robot


while fa.ReadMic() < clapSound:
   fa.LCDPrint(28, 0, "You need to clap to start")

fa.LCDClear()

timerStart = time.time()
while True:
    leftSensor = fa.ReadLine (0)
    rightSensor = fa.ReadLine (1)

    if rightSensor >= white and leftSensor >= white:
        fa.SetMotors (0, 0)
        print("Gap Detected")
        fa.LCDPrint(28, 0, "Gap Detected")
        break
    elif leftSensor >= white:
        fa.Right (correction)
    elif rightSensor >= white:
        fa.Left (correction)
    else:
        fa.SetMotors (50, 50)
        print(leftSensor, rightSensor)
timerStop = time.time()

travelTime = timerStop - timerStart

displayTravelTime = float("{:.2f}".format(travelTime))
fa.LCDPrint(28, 15, "Travel Time is:")
fa.LCDPrint(28, 25, displayTravelTime)
fa.LCDPrint(60, 25, "seconds")
print(displayTravelTime, " seconds")

fa.ComClose()
