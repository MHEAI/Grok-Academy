from microbit import *
import music

while True:
  if button_a.was_pressed():
    music.play(music.CHASE, wait=False, loop=True)
  if button_b.was_pressed():
    music.stop()