#!/usr/bin/python

from gpiozero import LED
from gpiozero import Button

led = LED(27)
button = Button(17)
while True :
    button.wait_for_press()
    led.on()
    button.wait_for_release()
    led.off()


