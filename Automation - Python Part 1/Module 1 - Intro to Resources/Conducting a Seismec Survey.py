from microbit import *

while True:
    if button_a.was_pressed():
        start = running_time()

    if button_b.was_pressed():
        end = running_time()
        delay = end - start
        distance = delay * 7 / 2
        display.scroll(str(distance))
