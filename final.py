#!/usr/bin/python

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD) # mode is in board so pin calls are pin numbers not gpio value.
pin_to_circuit = 7
import subprocess
from gpiozero import LED
from gpiozero import Button
import sys

led = LED(27)
button = Button(17)

# stop button funtion will end the program if the button is pushed.

def stop_button() :
    GPIO.setwarnings(False)
    GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_UP) # sets button to up at start of funtion.
    while True :
        input_state = GPIO.input(11) # if button is down the input is false if up it is true.
        if input_state == False :
            sys.exit()
        else :
            break

def rc_time(pin_to_circuit) :
    count = 0
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)
    GPIO.setup(pin_to_circuit, GPIO.IN)
   
    while (GPIO.input(pin_to_circuit) == GPIO.LOW) :
        count += 1
    if count > 3000 :
        subprocess.run(['./test']) # test is a bash script file on my system that prints date, time, and "it is dark"
        led.on()
    elif count < 2000 :
        led.off()
    count = count * 0
    stop_button() # calls to button control function.

def main() :

    loops = 0 
    while True :
        if loops == 0 :
            button.wait_for_press() # program waits to start until the user hits the button.
            loops += 1
            time.sleep(3) # program needs to sleep on start push or the program will close from the stop button function.
        elif loops > 0  :
            rc_time(pin_to_circuit)
        
    
main()
