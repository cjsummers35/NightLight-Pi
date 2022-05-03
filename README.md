# NightLight-Pi

This is a project for building a night light with a raspberry pi. 
When there is light in a room the led will be off and when there is low to no light the led will turn on.
There is a button that starts the program and ends the program.

In the light.py file there is code that makes the photoresistor work.
The program outputs a value assosiated with how much light is present.
If the light gets too dark the program will print some info from a test file on my pi.

In the LED_button.py there is code that allows for an led to be turned on and off with a button.

The test file has a bash script that prints the time and date and "it is dark." Note: in order to run the test file it needs to be executable, chmod can help with this.

The final.py is a merged version of the light.py and led_button.py where the light sensor controls the led power.
In the final.py the program wont run until the button is pushed and if pushed again the program will end.
When running the program will register light and if it is dark it prints "it is dark" and the led turns on and when dark the led turns off.

## Components:
- Rasperry Pi
- breadboard
- wires
- resistor
- capacitor
- photoresistor
- led
- button

## Circuit of night light:

First set up the button and LED :

![Screenshot (30)](https://user-images.githubusercontent.com/100862017/166481176-0b2c8521-4cd4-4b0c-a0de-bba1df3d72d5.png)

Seccond set up the photoresistor and capacitor :

![Screenshot (31)](https://user-images.githubusercontent.com/100862017/166481221-26ef2c18-8396-4bb0-ab8f-220fb1fee291.png)

After both are set up it should be something like this :

![Screenshot (29)](https://user-images.githubusercontent.com/100862017/166481276-5472135d-8c3f-4398-9257-5447d25cee2c.png)
