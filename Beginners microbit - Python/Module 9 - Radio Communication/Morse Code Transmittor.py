from microbit import *
import radio
radio.on()
while True:    
    if button_a.was_pressed():
        radio.send('dot')
        sleep(100)
    elif button_b.was_pressed():
        radio.send('dash')
        sleep(100)
