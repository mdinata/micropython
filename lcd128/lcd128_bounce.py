from machine import SPI, Pin, freq
from st7920_fb import ST7920
import time
import font454

freq(160000000)
display = ST7920(SPI(1, baudrate=8000000), Pin(5))
# display.text('Hello, world', 16, 30)
display.rect(0, 0, 128, 64, 1)
display.show()

boxw=5
boxh=5

boxposx=24
boxposy=24

boxspeedx=1
boxspeedy=1

width=128
height=64

while True:
    
    if boxposx > (width-boxw) or boxposx < 0:
        boxspeedx *= -1
    
    if boxposy > (height-boxh) or boxposy < 0:
        boxspeedy *= -1
    
    boxposx += boxspeedx
    boxposy += boxspeedy
    
    display.fill_rect(boxposx,boxposy,5,5,1)
    display.show()
    display.fill_rect(boxposx,boxposy,5,5,0)
