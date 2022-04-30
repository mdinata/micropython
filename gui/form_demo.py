from machine import Pin, I2C
import ssd1306
import time
from forms import *

i2c=I2C(scl=Pin(5), sda=Pin(4), freq=100000)
display=ssd1306.SSD1306_I2C(128,64,i2c)

f1=Form("Volume",0,0,20,10,invert=False,fill=True)
f2=Form("Total ",0,11,20,10,invert=True,fill=True)
f3=Form("/liter",0,22,20,10,invert=False,fill=True)

t1=Textbox("Pertamax",0,34)

display.show()
