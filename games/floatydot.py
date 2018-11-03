"""
Floaty Dot is flappy bird dot matrix implementation using Micropython
Written by Andi Dinata
November 3rd, 2018
"""

import max7219
from machine import Pin, SPI,freq, reset
import time
import urandom
import number

freq(160000000)
spi=SPI(1, baudrate=10000000, polarity=0, phase=0)
device=max7219.Matrix8x8(spi, Pin(2), 1)
device.fill(0)
device.brightness(10)
device.show()

s2=Pin(0,Pin.IN, Pin.PULL_UP)

score=0
def pipe():
    global score
    x=urandom.getrandbits(3)
    if x == 0:
        x = 1
    elif x > 4:
        x = 4
    for i in range(8):
        dot()
        device.hline(0,i,8,1)
        device.hline(x,i,3,0)
        device.show()
        time.sleep(0.05)
        device.scroll(0,1)
        device.hline(0,i,8,0)
        device.show()
        if i == 6:
            if x+3 > start_pos > x:
                score += 1
            else:
                gameover()
                
        if start_pos > 6 or start_pos < 1:
            gameover()

start_pos=2
def dot():
    global start_pos
    device.pixel(start_pos,6,1)
    device.show()
    time.sleep(0.05)
    device.pixel(start_pos,6,0)
    device.show()
    if s2.value():
        start_pos += 1
    else:
        start_pos -= 1
    return start_pos

def gameover():
    device.fill(0)
    device.show()
    number.draw(score)
    time.sleep(2)
    reset()
    
while True:
    pipe()
