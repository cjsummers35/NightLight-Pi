# NightLight-Pi

This is a project for building a night light with a raspberry pi. 
When there is light in a room the led will be off and when there is low to no light the led will turn on.
There will be a switch that can also turn the led on and off even in light.


## Components:
- Rasperry Pi
- breadboard
- wires
- resistor
- capacitor
- photoresistor
- led
- button

In the light.py file there is code that makes the photoresistor work with.
The program outputs a value assosiated with how much light is present.
If the light gets too dark the program will print some info from a test file on my pi.

In the LED_button.py there is code that allows for an led to be turned on and off with a button.

The final.py is a merged version of the light.py and led_button.py where the light sensor controls the led power.
In the final.py the program wont run until the button is pushed.
When pushed the program will register light and if it is dark it prints "it's dark" and the led turns on and when dark the led turns off.
