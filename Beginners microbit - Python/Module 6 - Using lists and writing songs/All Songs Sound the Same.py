from microbit import *
import music

NOTES = ["D4:4","D4:4","D4:4","D4:4","A3:4","A3:4","A3:4","A3:4","B3:4","B3:4","B3:4","B3:4","G3:4","G3:4","G3:4","G3:4",]

while True:
  if button_a.was_pressed():
    music.play(NOTES,loop=True,wait=False)
  if button_b.is_pressed():
    music.stop()