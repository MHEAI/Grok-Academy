from microbit import *
import music

playing = False

while True:
    if accelerometer.was_gesture('shake'):
        if playing:
            music.stop()
            display.clear()
            playing = False
        else:
            display.show(Image.MUSIC_QUAVERS)
            music.play(music.BLUES, loop=True, wait=False)
            playing = True
