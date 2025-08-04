from microbit import *
from microcar import *

def follow_line(max_speed):
  if max_speed < 130:
    max_speed = 130
  SLOW_SPEED = 100
  STOP_SPEED = 0
  position = detect_line()
  if position == 1:
    drive(max_speed, max_speed)
  elif position == 2:
    drive(SLOW_SPEED, SLOW_SPEED)
  elif position == 3:
    drive(SLOW_SPEED, max_speed)
  elif position == 4:
    drive(STOP_SPEED, max_speed)
  elif position == 5:
    drive(max_speed, SLOW_SPEED)
  elif position == 6:
    drive(max_speed, STOP_SPEED)

while True:
  sleep(10)
  follow_line(100)
