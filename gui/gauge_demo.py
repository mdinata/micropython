#Andi Dinata
#02 May 2022

import pcd8544_fb
from machine import Pin, SPI, ADC
import time
import font454 as sf
from gauge import Hbar

spi = SPI(1)
spi.init(baudrate=8000000, polarity=0, phase=0)
cs = Pin(2)
dc = Pin(15)
rst = Pin(0)
bl = Pin(16, Pin.OUT, value=0) # backlight on

display = pcd8544_fb.PCD8544_FB(spi, cs, dc, rst)

cpu=Hbar(display,"CPU :",0,0,20,10,1,1024)        
mem=Hbar(display,"RAM :",0,12,30,10,1,1024)
disk=Hbar(display,"Disk:",0,24,35,10,1,1024,step=0.2)

pot=ADC(0)

while True:
    pot_value=pot.read()

    cpu.value(pot_value,uom="%",series=True)
    mem.value(pot_value,uom="MB",series=True)
    disk.value(pot_value,uom="GB",series=True)
    
    time.sleep(0.1)
    display.show()
    
    cpu.clear()
    mem.clear()
    disk.clear()
