from microbit import *
from microcar import *

STOP_SPEED = 0
SLOW_SPEED = 100
FULL_SPEED = 255
while True:
  sleep(20)
  colour = detect_colour_rgb()
  if colour[0] > 150 and colour[1] < 100 and colour[2] < 100:
    drive(0,0)
    display.show(Image.SAD)
  else:
    position = detect_line()
    if position == 1:
      drive(FULL_SPEED,FULL_SPEED)
    elif position == 2:
      drive(SLOW_SPEED,SLOW_SPEED)
    elif position == 3:
      drive(SLOW_SPEED,FULL_SPEED)
    elif position == 4:
      drive(STOP_SPEED,FULL_SPEED)
    elif position == 5:
      drive(FULL_SPEED, SLOW_SPEED)
    elif position == 6:
      drive(FULL_SPEED,STOP_SPEED)
