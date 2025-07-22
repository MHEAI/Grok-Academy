from microbit import *
import music
import radio


radio.on()
DOT = Image('00000:'
            '00000:'
            '00900:'
            '00000:'
            '00000:')
DASH = Image('00000:'
             '00000:'
             '99999:'
             '00000:'
             '00000:')
while True:
  message = radio.receive()
  if message == 'dot':
    display.show(DOT)
    music.play('F5:1')
    display.clear()
    sleep(300)
  elif message == 'dash':
    display.show(DASH)
    music.play('F5:3')
    display.clear()
    sleep(300)