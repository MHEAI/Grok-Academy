from microbit import *
from microcar import *
import robot

while True:
    sleep(10)
    colour = detect_colour_rgb()
    
    if colour[0] > 150 and colour[1] < 100 and colour[2] < 100:
        leds_light_all([255, 0, 0])
        robot.follow_line(130)
    else:
        leds_light_all([0, 0, 0])
        robot.follow_line(250)
