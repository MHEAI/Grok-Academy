from microbit import *

count = 0
display.scroll(str(count))

while True:
    if button_a.was_pressed():
        count += 1
        display.scroll(str(count))
    if button_b.was_pressed():
        display.show(Image.NO)
        sleep(500)
        count = 0
        display.scroll(str(count))
