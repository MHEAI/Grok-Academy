from microbit import *

while True:
  display.show(Image.CHESSBOARD)
  sleep(1000)
  display.show(Image.CHESSBOARD.invert())
  sleep(1000)