from microbit import *
from microcar import *

LED_CYAN = (0, 255, 255)
LED_MAGENTA = (255, 0, 255)
LED_YELLOW = (255, 255, 0)
LED_BLACK = (0, 0, 0)

while True:
  leds_light_all(LED_CYAN)
  sleep(1000)
  leds_light_all(LED_BLACK)
  sleep(1000)
  leds_light_all(LED_MAGENTA)
  sleep(1000)
  leds_light_all(LED_BLACK)
  sleep(1000)
  leds_light_all(LED_YELLOW)
  sleep(1000)
  leds_light_all(LED_BLACK)
  sleep(1000)



