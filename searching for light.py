import FA
import time

fa = FA.Create()

fa.ComOpen(6)

fa.LCDClear()
treshold = 3000
pos = "A"
movement = 5

while True:
    illumination = fa.ReadLight()
    print(illumination)

    if (illumination > treshold):
        pos = "A"
        fa.Forwards(100)

    else:
        if pos == "A":
            pos = "B"
            fa.Left (movement)
        elif pos == "B":
            pos = "C"
            fa.Right(movement)
        elif pos == "C":
            pos = "D"
            fa.Right(movement)
        else:
            pos = "A"
            fa.Left (movement)

            if movement > 180:
                movement = movement + 5

            else:
                movement = 5
    time.sleep(2)
    break


fa.ComClose()
