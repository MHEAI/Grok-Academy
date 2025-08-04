from microbit import *

while True:
    x = accelerometer.get_x()
    y = accelerometer.get_y()

    if -100 <= x <= 100 and -100 <= y <= 100:
        display.show(Image.YES)
    else:
        display.show(Image.NO)
