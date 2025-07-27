import radio
from microbit import *


radio.on()
channel = 6
radio.config(channel=channel)
while True:
  if button_a.is_pressed():
    channel = 6
    radio.config(channel=channel)
  if button_b.is_pressed():
    channel = 9
    radio.config(channel=channel)
  message = radio.receive()
  if message is not None:
    display.show(Image(message))
