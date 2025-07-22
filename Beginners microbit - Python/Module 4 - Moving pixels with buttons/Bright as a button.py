from microbit import *

x = 0
while True:
  if button_a.was_pressed():
    if x >= 9 :
      continue
    x+=1
    display.set_pixel(2,2,x)
  
  