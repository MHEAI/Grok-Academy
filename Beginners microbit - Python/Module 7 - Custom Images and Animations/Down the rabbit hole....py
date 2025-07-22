from microbit import *

HOLE = Image('90009:'
             '90009:'
             '90009:'
             '90009:'
             '90099:'
             '90099:'
             '90009:'
             '90009:'
             '99009:'
             '99009:'
             '99009:'
             '90009:'
             '90099:'
             '90099:'
             '90099:'
             '90099:'
             '90009:'
             '99009:'
             '99009:'
             '99099:'
             '99999')
HEIGHT = 17
for i in range(HEIGHT):
  display.show(HOLE.shift_up(i))
  sleep(200)
display.show(Image.RABBIT)
