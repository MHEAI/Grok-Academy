from microbit import *
import music



while True:
  if button_a.was_pressed():
    music.play('F5:1')
  if button_b.was_pressed():
    music.play('F5:3')
