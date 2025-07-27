from microbit import *

display.show(Image.BUTTERFLY)

while True:
  if button_a.is_pressed():
    display.show(Image.HAPPY)
  elif button_b.is_pressed():
    display.show(Image.SILLY)
  else:
    display.show(Image.BUTTERFLY)