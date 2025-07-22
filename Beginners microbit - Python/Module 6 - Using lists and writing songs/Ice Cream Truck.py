from microbit import *
import music

GREENSLEEVES = ['A:2', 'C5:4', 'D:2', 'E:3', 'F:1', 'E:2', 'D:4', 'B4:2', 'G:3', 'A:1', 'B:2', 'C5:4', 'A4:2', 'A:3', 'G#:1', 'A:2', 'B:4', 'G#:2', 'E:4', 'A:2', 'C5:4', 'D:2', 'E:3', 'F:1', 'E:2', 'D:4', 'B4:2', 'G:3', 'A:1', 'B:2', 'C5:3', 'B4:1', 'A:2', 'G#:3', 'F#:1', 'G#:2', 'A:4', 'A:2', 'A:6']
POP_WEASEL = ['G:2', 'G:1', 'A:2', 'A:1', 'B', 'D5', 'B4', 'G:3', 'G:2', 'G:1', 'A:2', 'A:1', 'B:3', 'G', 'G:2', 'G:1', 'A:2', 'A:1', 'B', 'D5', 'B4', 'G:3', 'E5:3', 'A4:2', 'C5:1', 'B4:3', 'G']
BLUE_DANUBE = ['C4:2', 'E', 'G', 'G', 'R', 'G5', 'G', 'R', 'E', 'E', 'R', 'C4', 'C', 'E', 'G', 'G', 'R', 'G5', 'G', 'R', 'F', 'F', 'R', 'B3', 'B', 'D4', 'A', 'A', 'R', 'A5', 'A', 'R', 'F', 'F', 'R', 'B3']

while True:
  if button_a.is_pressed():
    music.play(GREENSLEEVES,loop =True,wait=False)
  elif button_b.is_pressed():
    music.play(POP_WEASEL,loop =True,wait=False)
  elif pin1.read_digital():
    music.play(BLUE_DANUBE,loop =True,wait=False)
  elif pin2.read_digital():
    music.stop()
    