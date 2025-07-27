import radio
from microbit import *


radio.on()
while True:
  radio.send('00900:00900:09990:99999:00900')
  sleep(5000)
