from microbit import *
import radio

radio.off()  

waiting = False

question_mark = Image("09990:90009:00990:00000:00900:")

while True:
    if button_a.was_pressed():
        radio.off()       
        radio.on()
        display.show(question_mark)
        waiting = True   
    
    if waiting:
        message = radio.receive()
        if message:
            waiting = False
            radio.send("win:" + message)
            display.scroll(message)
            display.clear()
