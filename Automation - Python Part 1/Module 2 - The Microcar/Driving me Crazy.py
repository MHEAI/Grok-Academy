from microbit import *
from microcar import *

for i in range(0,4,1):
  drive(255,255)
  sleep(3000)
  drive(0,0)
  display.show(Image.ARROW_S)
  sleep(2000)
  display.clear()
  drive(0,255)
  sleep(1750)
drive(0,0)