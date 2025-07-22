from microbit import *
import music

HANGMAN = [
  Image(),
  Image('90000:90000:90000:90000:90000'),
  Image('99990:90000:90000:90000:90000'),
  Image('99990:90090:90000:90000:90000'),
  Image('99990:90090:90090:90000:90000'),
  Image('99990:90090:90990:90000:90000'),
  Image('99990:90090:90999:90000:90000'),
  Image('99990:90090:90999:90090:90000'),
  Image('99990:90090:90999:90090:90900'),
  Image('99990:90090:90999:90090:90909')
]
index = 0
while True:
  if index == 9:
    music.play(music.POWER_DOWN)
    index = 0
  if button_a.was_pressed():
    index += 1
  display.show(HANGMAN[index%12])