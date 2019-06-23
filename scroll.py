import max7219
from machine import Pin, SPI,freq
import time

freq(160000000)
spi=SPI(1, baudrate=10000000, polarity=0, phase=0)
device=max7219.Matrix8x8(spi, Pin(2), 1)
device.brightness(10)
device.fill(0)
device.show()

s = 'Micropython is Cool'
for c in range(len(s)*8):
    device.fill(0)
    device.text(s,-c,0)
    device.show()
    time.sleep(0.05)    