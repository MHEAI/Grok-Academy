from microbit import *
import radio

radio.on()
radio.config(power=2)

MY_IMAGE = '09090:99999:99999:09990:00900'  # heart
ready = True

def process_image(image):
    display.show(Image(image))
    radio.send(image)
    sleep(700)
    display.clear()

while True:
    if button_a.was_pressed() and ready:
        process_image(MY_IMAGE)
        ready = False

    message = radio.receive()
    if message == MY_IMAGE and ready:
        sleep(500)
        process_image(MY_IMAGE)
        ready = False

    if button_b.was_pressed():
        ready = True
