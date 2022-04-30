#Nokia 5110 display initiation part
import pcd8544_fb
from machine import Pin, SPI

spi = SPI(1)
spi.init(baudrate=8000000, polarity=0, phase=0)
cs = Pin(2)
dc = Pin(15)
rst = Pin(0)
bl = Pin(16, Pin.OUT, value=0) # backlight on

display = pcd8544_fb.PCD8544_FB(spi, cs, dc, rst)

#the form library part
from form import *

f1=Form(display,"Volume",0,0,20,10,invert=False,fill=True)
f2=Form(display,"Total ",0,11,20,10,invert=True,fill=True)
f3=Form(display,"/liter",0,22,20,10,invert=False,fill=True)

t1=Textbox(display,"Pertamax",0,34)

display.show()
