from microbit import *

while True:
  if pin1.read_digital():
    display.clear()
    if button_a.is_pressed():
      display.show(Image.ARROW_N)
      
    if button_b.is_pressed():
      display.show(Image.ARROW_S)
  else:
     display.show(Image.ARROW_S)