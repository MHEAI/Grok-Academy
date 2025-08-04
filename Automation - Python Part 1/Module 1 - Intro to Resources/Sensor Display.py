from microbit import *
import radio

radio.on()

while True:
    message = radio.receive()
    if message:
        display.scroll(message)
