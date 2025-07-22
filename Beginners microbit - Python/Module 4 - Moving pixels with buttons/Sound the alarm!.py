from microbit import *
import music


count = 0
while True:
  if button_a.was_pressed():
    count = count + 1
  if button_b.is_pressed():
    display.show(Image.ASLEEP)
    sleep(count * 1000)
    display.clear()
    music.play(music.RINGTONE)
