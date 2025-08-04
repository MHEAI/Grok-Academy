from microbit import *
from microcar import *

while True:
  drive(255,255)
  sleep(3000)
  drive(0,0)
  display.show(Image.ARROW_S)
  sleep(2000)
  display.clear()