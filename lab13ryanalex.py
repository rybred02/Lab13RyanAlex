from gpiozero import LED, Button
from time import sleep
import random
led = LED(4)

right_button = Button(16)
left_button = Button(21)
def pressed(button):
    if button.pin.number == 14:
print(left_name + ‘ pressed first!’)
elif button.pin.number == 15:
print(right_name + ‘ pressed first!')
right_button.when_pressed = pressed
left_button.when_pressed = pressed

#This Lab is so broken and Alex and I have 0 patience*
