import radio
from microbit import *


radio.on()
while True:
  message = radio.receive()
  if message is not None:
    display.show(Image(message))
