from microbit import *
import radio

MY_ID = 'Seven'  
radio.on()

while True:
    if button_a.is_pressed():
        radio.send(MY_ID)

    message = radio.receive()
    if message:
        if message == 'win:' + MY_ID:
            display.show(Image.HAPPY)
            sleep(5000)
            display.clear()
        elif message.startswith('win:'):
            display.show(Image.SAD)
            sleep(5000)
            display.clear()
