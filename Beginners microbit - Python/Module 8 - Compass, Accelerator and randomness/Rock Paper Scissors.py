from microbit import *
import random

ROCK = Image('09990:99999:99999:99999:09990')
PAPER = Image.SQUARE
SCISSORS = Image('90099:09099:00900:09099:90099')

MOVES = [ROCK,PAPER,SCISSORS]

while True:
  if button_a.is_pressed():
    display.scroll("321")
    display.show(random.choice(MOVES))
    sleep(10000000)