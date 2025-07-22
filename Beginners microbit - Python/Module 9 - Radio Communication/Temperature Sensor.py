from microbit import *
import radio

radio.on()
radio.config(channel=7, power=7)

while True:
    temp = temperature()
    radio.send(str(temp))
    sleep(3000)
