from microbit import *
import radio

channel = 6
radio.config(channel=channel)
radio.on()
display.clear()

last_received = running_time()
showing = False

while True:
    if button_a.was_pressed():
        display.clear()
        channel = (channel - 1) % 10
        radio.config(channel=channel)
        display.clear()
        showing = False

    if button_b.was_pressed():
        display.clear()
        channel = (channel + 1) % 10
        radio.config(channel=channel)
        display.clear()
        showing = False

    msg = radio.receive()
    if msg:
        try:
            img = Image(msg)
            display.show(img)
            last_received = running_time()
            showing = True
        except:
            pass

    if showing and running_time() - last_received > 1000:
        
        showing = False

    sleep(50)
