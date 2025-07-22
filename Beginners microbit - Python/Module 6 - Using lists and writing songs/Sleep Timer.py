from microbit import *
import music

LULLABY = [
  'E4:2', 'E', 'G:8',
  'E:2', 'E', 'G:8',
  'E:2', 'G', 'C5:4', 'B4', 'A', 'A', 'G',
  'D:2', 'E', 'F:4', 'D', 'D:2', 'E', 'F:8',
  'D:2', 'F', 'B', 'A', 'G:4', 'B', 'C5:8'
]

clocks = list(Image.ALL_CLOCKS)
index = 0
display.show(clocks[index])

while True:
    if button_a.was_pressed():
        index = (index + 1) % len(clocks)
        display.show(clocks[index])

    if button_b.was_pressed():
        if index == 0:
            continue
        display.show(Image.ASLEEP)
        music.play(LULLABY,wait=False,loop =True)
        sleep(5000 * index)
        index = 0
        display.show(clocks[0])  