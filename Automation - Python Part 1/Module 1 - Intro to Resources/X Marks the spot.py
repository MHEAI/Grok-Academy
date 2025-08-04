from microbit import *

while True:
    display.set_pixel(0, 0, 9)
    display.set_pixel(0, 4, 9)
    display.set_pixel(4, 0, 9)
    display.set_pixel(4, 4, 9)
    sleep(500)

    display.set_pixel(1, 1, 9)
    display.set_pixel(1, 3, 9)
    display.set_pixel(3, 1, 9)
    display.set_pixel(3, 3, 9)
    sleep(500)

    display.set_pixel(2, 2, 9)
    sleep(500)

    display.clear()
    sleep(500)
