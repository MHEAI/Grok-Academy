from microbit import *
import music

while True:
  if button_a.was_pressed():
     display.show(Image.DIAMOND)
     music.play(music.BA_DING)
     display.clear()