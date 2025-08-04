from microbit import *
from microcar import *

FULL_SPEED = 255
SLOW_SPEED = 100
STOP_SPEED = 0
while True:
  sleep(10)
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
