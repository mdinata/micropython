#Andi Dinata
#June 2022

import pcd8544_fb
from machine import Pin, SPI, I2C
import os
import time
import pcf8574

i2c=I2C(scl=Pin(5), sda=Pin(4))
button=pcf8574.PCF8574(i2c,0x20)

spi = SPI(1)
spi.init(baudrate=8000000, polarity=0, phase=0)
cs = Pin(2)
dc = Pin(15)
rst = Pin(0)
bl = Pin(16, Pin.OUT, value=1) # backlight on

display = pcd8544_fb.PCD8544_FB(spi, cs, dc, rst)

if os.getcwd() == '/':
    os.chdir('asset')

bird = display.sprite('bird0.pbm',14,10)
floor = display.sprite('floor.pbm',168,48)
pipe = display.sprite('pipeseg.pbm',14,5)
pipeend = display.sprite('pipeend.pbm',16,7)

birdx,birdy = 14,16
floorx,floory = 0,0
pipex,pipey = 60,0 

def update():
    display.blit(floor,floorx,floory)
    display.blit(bird,birdx,birdy)
    
def draw_pipe(n):
    for i in range(n):
        display.blit(pipe,pipex,i*5)
    display.blit(pipeend,pipex-1,(i*5)+5)    #top end
    top = (i*5) + 5
    
    for i in range(n):
        display.blit(pipe,pipex,35-i*5)
    display.blit(pipeend,pipex-1,35-(i*5)-5) #bottom end
    bottom = 35 -(i*5) - 5
    
    return (top,bottom)
    
def check(birdy):
    if birdy < 0: birdy = 0
    if birdy > 30: birdy = 30
    return birdy

def check_collission(birdx,birdy,pipex,top,bottom):
    if (birdx + 14 >= pipex) and (birdx + 10 <= pipex + 14):
        if birdy <= top or birdy + 10 >= bottom:
            return True
    
frame=0
dx=0
gameover = False

while True:
    frame += 1
    
    birdy=check(birdy)
    update()
    top,bottom = draw_pipe(1)
    
    gameover = check_collission(birdx,birdy,pipex,top,bottom)
    
    if gameover: break
    
    if frame%2 == 0:
        floorx -= 1
        pipex -= 1
        if floorx < -84: floorx = 0
        if pipex < -20: pipex = 90
            
    if frame%3 == 0:
        if button.pin(6) == 0: birdy -= 3
        else: birdy += 1
    
    display.show()
    
    time.sleep(0.02)
