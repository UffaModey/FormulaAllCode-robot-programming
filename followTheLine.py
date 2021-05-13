import time
import FA

fa = FA.Create()
fa.ComOpen(6)

fa.LCDClear()

white = 200 #Reflection value from a white surface
correction = 10 #correction angle
clapSound = 3000 #clap treshold to trigger motion of the robot


#while fa.ReadMic() < clapSound:
   #fa.LCDPrint(28, 0, "You need to clap to start")

fa.LCDClear()

timerStart = time.time()
while True:
    left_sensor = fa.ReadLine (0)
    right_sensor = fa.ReadLine (1)

    if right_sensor >= white and left_sensor >= white:
        fa.SetMotors (0, 0)
        print("Gap Detected")
        fa.LCDPrint(28, 0, "Gap Detected")
        break
    elif left_sensor >= white:
        fa.Right (correction)
    elif right_sensor >= white:
        fa.Left (correction)
    else:
        targetPosition = left_sensor + right_sensor
        currentPosition = left_sensor + right_sensor
        
        error = targetPosition - currentPosition

        while (error
        fa.SetMotors (50, 50)
        print(left_sensor, right_sensor)
timerStop = time.time()

travelTime = timerStop - timerStart

displayTravelTime = float("{:.2f}".format(travelTime))
fa.LCDPrint(28, 15, "Travel Time is:")
fa.LCDPrint(28, 25, displayTravelTime)
fa.LCDPrint(60, 25, "seconds")
print(displayTravelTime, " seconds")

fa.ComClose()
