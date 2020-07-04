# Add your Python code here. E.g.
from microbit import *
import random

display.scroll('GET READY > >',delay =100)
score = 0

arrows = [Image.ARROW_W, Image.ARROW_E, Image.ARROW_S, Image.ARROW_N]
times = []

gameOn = True
display.clear()
while gameOn:
    image = random.choice(arrows)
    display.clear()
    display.show(image)
    start_time = running_time()
    testOn = True
    while testOn:
        if image == Image.ARROW_S and accelerometer.get_y() < -1500:
            t = round(running_time() - start_time) /10
            times.append(t)
            testOn = False
        if image == Image.ARROW_N and accelerometer.get_y() > 1500:
            t = running_time() - start_time
            times.append(t)
            testOn = False
        if image == Image.ARROW_W and accelerometer.get_x() < -1500:
            t = running_time() - start_time
            times.append(t)
            testOn = False
        if image == Image.ARROW_E and accelerometer.get_x() > 1500:
            t = running_time() - start_time

