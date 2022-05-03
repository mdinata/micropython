#Andi Dinata
#01 May 2002

#oled display initiation part
from machine import Pin, I2C
import ssd1306
import time

i2c=I2C(scl=Pin(5), sda=Pin(4), freq=100000)
display=ssd1306.SSD1306_I2C(128,64,i2c)

#form library part
from forms import *

f1=Form(display,"Volume",0,0,20,10,invert=False,fill=True)
f2=Form(display,"Total ",0,11,20,10,invert=True,fill=True)
f3=Form(display,"/liter",0,22,20,10,invert=False,fill=True)

t1=Textbox(display,"Pertamax",0,34)

display.show()
