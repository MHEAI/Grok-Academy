import radio
from microbit import *


radio.on()
question = '09990:90009:00990:00000:00900'
while True:
  message = radio.receive()
  if message is not None:
    if message.startswith('jeff:'):
      radio.send('what?')
      display.show(Image(question))
      sleep(3000)
      display.clear()
    else:
      display.scroll('zzz')
