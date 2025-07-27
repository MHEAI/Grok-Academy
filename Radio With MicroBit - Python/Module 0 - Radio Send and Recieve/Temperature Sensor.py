import radio
from microbit import *


radio.on()
while True:
  radio.send(str(temperature()))
  sleep(3000)
