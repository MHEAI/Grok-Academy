from microbit import *

display.show(Image.BUTTERFLY)

while True:
  if button_a.is_pressed() and button_b.is_pressed():
    display.show(Image.CONFUSED)
  elif button_b.is_pressed():
    display.show(Image.SILLY)
  elif button_a.is_pressed():
    display.show(Image.HAPPY)
  else:
    display.show(Image.BUTTERFLY)