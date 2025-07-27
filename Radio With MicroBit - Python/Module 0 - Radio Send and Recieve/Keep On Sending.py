from microbit import *
import radio


radio.on()
while True:
  radio.send('ahoy!')
  sleep(5000)
