import radio
from microbit import *


radio.on()
radio.config(channel=12)
ready = False
QUESTION_MARK = Image('09990:90009:00990:00000:00900')
while True:
  if button_a.was_pressed():
    radio.send('awdawdawd')
  if button_b.was_pressed():
    ready = True
    display.show(QUESTION_MARK)
  message = radio.receive()
  if message is not None:
    if ready == True:
      display.scroll(message)
      ready = False
