# Micropython wrapper
Micropython wrapper script for ESP8266 based microcontroller

This repository contains the wrapper for interacting with GPIO pin, sensor, display and webserver

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

For micropython asyncio, get the latest from https://github.com/peterhinch/micropython-async/. Make directory on your ESP board named uasyncio and put synchro.py, .__init__.py, queues.py and core.py. Make another directory called collections and put deque.py inside

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
#### usage:
```
from uGPIO import GPIO
GPIO.help()

output will be:
Cheat Sheet Wemos D1 Mini
-------------------------
                   ____________
                  /            |
             RST-|         =   |- TX
              A0-|   ESP8266   |- RX
NO PWM GPIO16 D0-|         SCL-|- D1 GPIO5
       GPIO14 D5-|-SCK     SDA-|- D2 GPIO4
       GPIO12 D6-|-MISO        |- D3 GPIO0 PullUp
       GPIO13 D7-|-MOSI        |- D4 GPIO2 PullUp Built-in Led
PullDn GPIO15 D8-|             |- G
             3v3-|_____________|- 5V

#pin on/off
p=GPIO(12)  #initiate pin 12 with default PWM inactive
p.on()      # GPIO on
p.off()     # GPIO off

#pin on/off in loop (e.g. blinking led)
p.repeat(5)     # loop for 5 times at default delay time 0.5 second
p.repeat(5,0.1) # loop for 5 times at custom delay time e.g. 0.1 second

#pin toggle to turn on and off with the same function
p.toggle()      # turn on
p.toggle()      # turn off

#use PWM
p=GPIO(12,1)  # initiate pin 12 with PWM flag active with default frequency at 500
p.scale(50)   # change duty cycle in 1-100. 0 = off, 1 = minimum, 100 = maximum
p.fade_in()   # to increase the led brightness gradually. Default step=5, t=0.1. Change step and t for smoother effect.
p.fade_out()  # to decrease the led brightness gradually. Default step=5, t=0.1. Change step and t for smoother effect.
```

### usensor.py
Wrapper to simplify the operation of ultrasonic HC-SR04.
```
from usensor import Ultrasonic
us=Ultrasonic(5,4)      # initiate sensor with trigger at Pin 5 and echo at Pin 4. Change it according your setup
```
#### usage:
```
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
l=LCD()

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
#### usage:
```
l.help()            # print help
l.text("hello")     # display text 'hello' on the screen with default position
l.move(7,1)         # change start position at column 5 at 2nd line
l.text("world")     # display text world at the new position
l.scroll('hi')      # scroll the text 'hi' from left to right. default delay 0.5s
l.scroll('hi',0.1)  # scroll text at custom speed
l.clear()           # clear the screen
```
### async_demo.py
Wrapper to get micropython async programming running on your ESP8266 board. Demo is using RGB led where each led has different cycles and seemingly running parallel. By default Red color use Pin 15, Green use Pin 12 and Blue use Pin 13. Specify your own Pin for each color.
```
from async_demo import RGB
l=RGB()
```
or:
```
l=RGB(15,12,13)
```
#### usage:
```
l.rainbow()       #each color will fade in/out with different timnig seemingly parallel and produces new color
l.disco()         #each color will turn on/off with different timing like disco light
```
Be sure to soft-reset the board (Ctrl-D) before switching from rainbow and disco. It is known bug, the loop close does not clear the task queue.

### webit.py
This wrapper help your measurement data published to webpage in no time. Call your main function to measure from webit to get it published in website. The refresh button in webpage allows you to refresh the individual reading. If you are connected to micropython access point e.g. MicroPython-XXXXXX, go to address 192.168.4.1 from your web browser.
#### usage:
```
from webit import Webserver
w=Webserver()
w.start()
```
### music.py
This is wrapper for music jukebox with micropython. One song is added at the time being. Set the pin where your buzzer is connected e.g. Pin14 and set the led pin to flash along the playing tone. If led pin is not specified, it will use Pin2 (on board led).
#### usage:
```
from music import Music
m=Music(14,16)
m.play(1)
```
