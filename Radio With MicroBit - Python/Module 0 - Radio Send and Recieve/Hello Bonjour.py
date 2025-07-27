import radio
from microbit import *


radio.on()
while True:
  if button_a.is_pressed():
    radio.send('hello')
  if button_b.is_pressed():
    radio.send('bonjour')
