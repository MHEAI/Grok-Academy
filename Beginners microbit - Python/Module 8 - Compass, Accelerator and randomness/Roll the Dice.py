from microbit import *
import random


DICE = [Image('00000:''00000:''00900:''00000:''00000:'),Image('90009:''00000:''00000:''00000:''90009:'),Image('90000:''00000:''00000:''00000:''00009:'),Image('90009:''00000:''00900:''00000:''90009:'),Image('00009:''00000:''00900:''00000:''90000:'),Image('90009:''00000:''90009:''00000:''90009:')]

while True:
  if accelerometer.was_gesture("shake"):
    display.clear()
    sleep(300)
    
    display.show(random.choice(DICE))
    