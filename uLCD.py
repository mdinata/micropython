# micropython LCD wrapper for ESP8266 based board
# written by Andi Dinata
# under MIT License
# library esp8266_i2c_lcd source is https://github.com/dhylands/python_lcd 

from machine import I2C, Pin
from esp8266_i2c_lcd import I2cLcd
import time

addr = 0x27
width = 16
str_pad = " " * width

class LCD():
    def __init__(self):
        self.i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
        self.lcd = I2cLcd(self.i2c, addr, 2, 16)

    def text(self,string):
        self.lcd.putstr(string)
    
    def scroll(self,string,t=0.5):
        self.clear()
        string= str_pad + string
        for i in range(0,len(string)):
            long_string=string[i:(i+width)]
            self.text(long_string)
            time.sleep(t)
            self.text(str_pad)
            self.clear()

    def clear(self):
        self.lcd.clear()

    def hide(self):
        self.lcd.display_off()

    def show(self):
        self.lcd.display_on()

    def move(self,x,y):
        self.lcd.move_to(x,y)

    def on(self):
        self.lcd.backlight_on()

    def off(self):
        self.lcd.backlight_off()

    def help(self):
        print('Cheat sheet')
        print('-----------')
        print('text = put string on screen, default position column 1, line 1')
        print('scroll = scroll the text from left to right, default position line 1')
        print('move = move to position x,y. x=0 means line 1, y=0 means col 1')
        print('on   = backlight on')
        print('off  = backlight off')
        print('hide = hide content displayed')
        print('show = show content displayed')
        print('clear= clear the screen and content')
        
