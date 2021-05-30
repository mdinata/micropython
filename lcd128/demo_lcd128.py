from st7920 import Screen
from gfx import GFX
from sysfont import sysfont
import machine
import time

machine.freq(160000000)
spi = machine.SPI(1, baudrate=80000000, polarity=1, phase=1)
screen = Screen(slaveSelectPin=Pin(15), resetDisplayPin=Pin(5))
draw=GFX(128,64,screen.plot)
#screen.set_rotation(2)
screen.clear()

def test1():
    t0=time.ticks_ms()
#     screen.fill_rect(0,0,127,63)
    screen.redraw()
    t1=time.ticks_ms()
    delta=time.ticks_diff(t1,t0)
    print(delta/1000)

def test2():
    t0=time.ticks_ms()
#     draw.fill_rect(0,0,128,64,1)
    screen.redraw()
    t1=time.ticks_ms()
    delta=time.ticks_diff(t1,t0)
    print(delta/1000)


test1()
test2()