from microbit import *
from microcar import *

def follow_line():
  FULL_SPEED = 255
  SLOW_SPEED = 100
  STOP_SPEED = 0
  result = detect_line()
  if result==1:
    drive(FULL_SPEED, FULL_SPEED)
  elif result==2:
    drive(SLOW_SPEED , SLOW_SPEED)
  elif result==3:
    drive(SLOW_SPEED , FULL_SPEED)
  elif result==4:
    drive(STOP_SPEED, FULL_SPEED)
  elif result==5:
    drive(FULL_SPEED, SLOW_SPEED)
  elif result==6:
    drive(FULL_SPEED, STOP_SPEED)

while True:
  sleep(10)
  follow_line()
