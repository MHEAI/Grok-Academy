from microbit import *

while True:
  heading = int(compass.heading())
  index = -int(heading/30)
  display.show(Image.ALL_CLOCKS[index])