from microbit import *

from microbit import *

while True:
  if button_a.is_pressed():
    display.show(Image.HAPPY)
  else:
    display.show(Image.SAD)