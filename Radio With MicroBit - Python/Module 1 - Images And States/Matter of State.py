import radio
from microbit import *


radio.on()
sent = False
while True:
  if button_a.was_pressed() and sent == False:
    radio.send('awdawdawd')
    sent = True
  if button_b.was_pressed():
    sent = False
