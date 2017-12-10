# Micropython wrapper
Micropython wrapper script for ESP8266 based microcontroller

This repository contains the wrapper for interacting with GPIO pin, sensor and displays.

## Prerequisite
For LCD, the LCD1602 driver source is located at https://github.com/dhylands/python_lcd. Clone this repository first then copy these files to your ESP8266 board using adafruit-ampy or webrepl:
```
sudo ampy -b 115200 -p /dev/ttyUSB0 put esp8266_i2c_lcd.py
sudo ampy -b 115200 -p /dev/ttyUSB0 put lcd_api.py
```
Connect your LCD1602<br >
--------------------<br >
SCL --> D1 (GPIO5)<br >
SDA --> D2 (GPIO4)<br >
VCC --> 5v <br >
GND --> G<br >

## Installing
Clone this repository and copy the .py to your ESP8266 board. You can use adafruit-ampy tool to copy to your ESP8266 board

```
sudo ampy -b 115200 -p /dev/ttyUSB0 put uGPIO.py
sudo ampy -b 115200 -p /dev/ttyUSB0 put usensor.py
sudo ampy -b 115200 -p /dev/ttyUSB0 put uLCD.py
```

## Usage
### uGPIO.py
A generic wrapper to interact with GPIO pin. One wrapper works for Led, Buzzer, RGB led, PWM Led, Servo motor. <br >
Each .py contains handy help print out <br >
Examples:
```
from uGPIO import GPIO
GPIO.help()

output will be:
Cheat Sheet
--------------------------------------
D0 IO                           GPIO16
D1 IO SCL                       GPIO5
D2 IO SDA                       GPIO4
D3 IO 10k Pull Up               GPIO0
D4 IO 10k Pull Up, Built-in Led GPIO2
D5 IO SCK                       GPIO14
D6 IO MISO                      GPIO12
D7 IO MOSI                      GPIO13
D8 IO 10k Pull Down             GPIO15
All Pins have PWM except D0

#pin on/off
p=GPIO(12)  #initiate pin 12 with default PWM inactive
p.on()      # GPIO on
p.off()     # GPIO off

#pin on/off in loop (e.g. blinking led)
p.repeat(5)     # loop for 5 times at default delay time 0.5 second
p.repeat(5,0.1) # loop for 5 times at custom delay time e.g. 0.1 second

#use PWM
p=GPIO(12,1)  # initiate pin 12 with PWM flag active with default frequency at 500
p.scale(50)   # change duty cycle in 1-100. 0 = off, 1 = minimum, 100 = maximum
```

### usensor.py
Wrapper to simplify the operation of ultrasonic HC-SR04.
```
from usensor import Ultrasonic
us=Ultrasonic(5,4)      # initiate sensor with trigger at Pin 5 and echo at Pin 4. Change it according your setup

#get distance and return single measurement
us.get_distance()       # read the distance. cm is default unit of measure
us.get_distance("mm")   # read output in milimeter
us.get_distance("m")    # read output in meter

#get distance from multiple measurement and return average value
us.get_average()        # read average distance from a 3 measurement (default) in cm
us.get_average(5,"mm")  # read average distance from custom individual value in custom unit of measure
```
### uLCD.py
Wrapper to simplify the operation of LCD1602 display with I2C Backpack.
```
from uLCD import LCD
l=LCD() # initiate LCD

#print out help
l.help()

Cheat sheet
----------------------------------------------------------------
text   = put string on screen, default position column 1, line 1
move   = move to position x,y. x=0 means line 1, y=0 means col 1
on     = backlight on
off    = backlight off
hide   = hide content displayed
show   = show content displayed
clear  = clear the screen and content
scroll = scroll the text from left to right
```
#### examples:
d.text("hello") # display text hello on the screen with default position
d.move(7,1)     #change start position at column 5 at 2nd line
d.text("world") # display text world at the new position
d.clear()       # clear the screen
```
