from microbit import *
import music

from microbit import *
import music

x = 0
y = 0
while True:
  display.set_pixel(x, y, 9)
  
  if x == 4 and y == 4:
    music.play(music.POWER_UP)
    display.clear()
    x = 0
    y = 0
  if button_a.was_pressed():
    x = x + 1
    if x > 4:
      x -= 1

  if button_b.was_pressed():
    y = y + 1
    if y > 4:
      y -= 1