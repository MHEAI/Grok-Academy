from microbit import *
import music


while True:
  temp = temperature()
  strt = str(temp)
  if strt == "38" or strt == "37":  
    music.stop()
    display.show(Image.HAPPY)
  else:
    music.play("C6:4", loop = True,wait = False)
    display.scroll(strt)
   