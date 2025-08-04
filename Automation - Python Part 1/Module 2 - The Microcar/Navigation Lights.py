from microbit import *
from microcar import *

LED_GREEN = (0, 255, 0)
LED_RED = (255, 0, 0)
leds_light_single(0, LED_GREEN)
leds_light_single(1, LED_GREEN)
leds_light_single(2, LED_RED)
leds_light_single(3, LED_RED)
for i in range(0,5,1):
  drive(255,255)
  sleep(3000)
  drive(0,0)
  display.show(Image.ARROW_S)
  sleep(2000)
  display.clear()