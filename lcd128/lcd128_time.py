from st7920 import Screen
from gfx import GFX
from sysfont import sysfont
import machine
import time

machine.freq(160000000)
spi = machine.SPI(1, baudrate=80000000, polarity=1, phase=1)
screen = Screen(slaveSelectPin=Pin(15), resetDisplayPin=Pin(0))
draw=GFX(128,64,screen.plot)

screen.clear()

timestr=[]

def update():
    now=time.localtime()
    return now

def add_zero(element):
    if len(str(element)) < 2:
        element="0{}".format(element)
        
    timestr.append(element)
    
def clearheader():
    draw.fill_rect(1,1,124,8,0)

def frame():
    #header
    draw.rect(0,0,127,11,1)

def showtime():
    for element in time.localtime():
        add_zero(element)
        
    finalstr="{}-{}-{}  {}:{}:{}".format(timestr[2],timestr[1],timestr[0],timestr[3],timestr[4],timestr[5])
    
    screen.text((4,2),finalstr,sysfont,1)
    screen.redraw()

import framebuf

def load_image(filename):
    with open(filename, 'rb') as f:
        f.readline()
        f.readline()
        data = bytearray(f.read())
    return framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)
import os
os.chdir('img')
img=load_image('background.pbm')
display.blit(img,0,0)
display.show()

frame()
while True:
    showtime()
    time.sleep(1)
    timestr=[]
    clearheader()
    