from microbit import *

start = running_time()
message = "Do not press the buttons."

while True:
    for char in message:
        display.show(char)
        sleep(200)  
        if button_a.was_pressed() or button_b.was_pressed():
            break
    else:
        continue
    break

end = running_time()
total_time = (end - start) // 1000  

display.scroll("You lasted " + str(total_time) + "s")
