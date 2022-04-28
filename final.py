#!/usr/bin/python

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
pin_to_circuit = 7
import subprocess
from gpiozero import LED
from gpiozero import Button

led = LED(27)
button = Button(17)


def rc_time(pin_to_circuit) :
    count = 0
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)
    GPIO.setup(pin_to_circuit, GPIO.IN)
   
    while (GPIO.input(pin_to_circuit) == GPIO.LOW) :
        count += 1
    if count > 3000 :
        subprocess.run(['./test'])
        led.on()
    elif count < 2000 :
        led.off()
    count = count * 0

def main() :

    loops = 0 
    while True :
        if loops == 0 :
            button.wait_for_press()
            loops += 1
        elif loops > 0  :
            rc_time(pin_to_circuit)
        
    
main()
