from microbit import *
import music

while True:
    if button_a.was_pressed():
        sleep(3000)
        display.show(Image.TARGET)
        music.play("C:4",wait =False) 
        start = running_time()
    if button_b.was_pressed():
        end = running_time()
        time = str(end - start)
        display.scroll(time + "ms")

