from microbit import *
import music

while True:
  if button_a.is_pressed():
    display.show(Image.SAD)
    music.play(music.WAWAWAWAA)
    display.clear()