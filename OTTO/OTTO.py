"""
OTTO DIY Robot with Micropython
Written by Andi Dinata under MIT license
February 2018
"""

from machine import Pin, PWM
from time import sleep, sleep_ms

RB_flat=75 #75
LB_flat=80 #80
RF_flat=75 #75
LF_flat=69 

LB=PWM(Pin(2),freq=50)
LF=PWM(Pin(0),freq=50)
RB=PWM(Pin(5),freq=50)
RF=PWM(Pin(4),freq=50)


def help():
  f=open('OTTO.txt','r')
  for i in range(20):
    print(f.readline().rstrip('\n\r'))
  f.close()
  

def standby():
  RB.duty(RB_flat)
  LB.duty(LB_flat)
  sleep_ms(10)
  RF.duty(RF_flat)
  LF.duty(LF_flat)

def updown(n):
  for i in range(n):
    RF.duty(RF_flat-25)
    sleep_ms(10)
    LF.duty(LF_flat+25)
    sleep(0.5)
    RF.duty(RF_flat)
    sleep_ms(10)
    LF.duty(LF_flat)
    sleep(0.5)
    
def left():
  LF.duty(LF_flat+41)
  sleep(0.2)
  RF.duty(RF_flat+25) #30
  sleep(1)
  LF.duty(LF_flat-19)
  sleep(0.2)
  RF.duty(RF_flat-25) #30
  sleep(0.5)

def right():
  RF.duty(RF_flat-30)
  sleep(0.2)
  LF.duty(LF_flat-22) #25
  sleep(1)
  RF.duty(RF_flat+22)
  sleep(0.2)
  LF.duty(LF_flat+31)
  sleep(0.5)
  
def lstep():
  LF.duty(LF_flat+41)
  sleep(0.2)
  RF.duty(RF_flat+28) #30
  sleep(0.1)
  for i in range(10):
    RB.duty(RB_flat-i)
    sleep_ms(10)
  for i in range(15):
    LB.duty(LB_flat-i)
    sleep_ms(10)
  LF.duty(LF_flat)
  sleep(0.1)
  RF.duty(RF_flat)

def rstep():
  RF.duty(RF_flat-30)
  sleep(0.2)
  LF.duty(LF_flat-24)
  sleep(0.1)
  for i in range(8):
    LB.duty(LB_flat+i) 
    sleep_ms(10)
  for i in range(13):
    RB.duty(RB_flat+i)
    sleep_ms(10)
  sleep(0.1)
  RF.duty(RF_flat)
  sleep(0.1)
  LF.duty(LF_flat)

def lbstep():
  LF.duty(LF_flat+41)
  sleep(0.2)
  RF.duty(RF_flat+25) #30
  sleep(0.1)
  RB.duty(88)
  sleep(0.1)
  LB.duty(88)
  sleep(0.1)
  LF.duty(LF_flat)
  sleep(0.1)
  RF.duty(RF_flat)

def rbstep():
  RF.duty(RF_flat-30)
  sleep(0.2)
  LF.duty(LF_flat-22)
  sleep(0.1)
  LB.duty(65) 
  sleep(0.1)
  RB.duty(65) 
  sleep(0.1)
  RF.duty(RF_flat)
  sleep(0.1)
  LF.duty(LF_flat)
  
def zigzag(n):
  for i in range(n):
    LB.duty(100)
    sleep_ms(10)
    RB.duty(60)
    sleep(0.2)
    LB.duty(60)
    sleep_ms(10)
    RB.duty(95)
    sleep(0.2)
    

#Final Functions    
def wiggle(direction,step):
    if direction == 'left':
      LF.duty(LF_flat+41)
      sleep(0.2)
      RF.duty(RF_flat+25) #30
      sleep(1)
      for i in range(step):
        LF.duty(LF_flat+31)
        sleep(0.1)
        LF.duty(LF_flat-9)
        sleep(0.1)
      sleep(0.2)
      LF.duty(LF_flat)
      sleep_ms(10)
      RF.duty(RF_flat)
    elif direction == 'right':
      RF.duty(RF_flat-30)
      sleep(0.2)
      LF.duty(LF_flat-22) #25
      sleep(1)
      for i in range(step):
        RF.duty(RF_flat-20)
        sleep(0.1)
        RF.duty(RF_flat+30)
        sleep(0.1)
      RF.duty(RF_flat)
      sleep(0.2)
      LF.duty(RF_flat)

def tilt(direction):
  if direction == 'left':
    LF.duty(LF_flat+41)
    sleep(0.2)
    RF.duty(RF_flat+25) #30
    sleep(2)
    LF.duty(LF_flat)
    sleep(0.2)
    RF.duty(RF_flat)
  elif direction == 'right':
    RF.duty(RF_flat-30)
    sleep(0.2)
    LF.duty(LF_flat-25) #25
    sleep(2)
    RF.duty(RF_flat)
    sleep(0.2)
    LF.duty(LF_flat)
    
def turn(direction,step):
  if direction == 'right':
    for i in range(step):
      RF.duty(RF_flat-30)
      sleep(0.2)
      LF.duty(LF_flat-22)
      for i in range(30):
        LB.duty(LB_flat+i)
        sleep_ms(20)
      RF.duty(RF_flat)
      sleep(0.1)
      LF.duty(LF_flat)
      sleep(0.1)
      LB.duty(LB_flat-10)
      sleep(0.1)
  elif direction == 'left':
    for i in range(step):
      LF.duty(LF_flat+41)
      sleep(0.2)
      RF.duty(RF_flat+28)
      for i in range(25):
        RB.duty(RB_flat-i)
        sleep_ms(20)
      LF.duty(LF_flat)
      sleep(0.1)
      RF.duty(RF_flat)
      sleep(0.1)#LB
      RB.duty(RB_flat-10)
      sleep(0.1)

       
def move(direction,step,speed=500):
  if direction == 'forward':
    for i in range(step):
      lstep()
      sleep_ms(speed)
      rstep()
      sleep_ms(speed)
  elif direction == 'back':
    for i in range(step):
      lbstep()
      sleep_ms(speed)
      rbstep()
      sleep_ms(speed)
  

def strafe(direction, step):
  for i in range(step):
      if direction == 'left':
        left()
      elif direction == 'right':
        right()
        
def moonwalk(direction,step,height=25,speed=10):
  l_up_pos=0
  l_down_pos=0
  r_up_pos=0
  r_down_pos=0
  
  if direction == 'right':
    RB.duty(65)
    sleep_ms(20)
    LB.duty(65)
    for i in range(step):  
      for i in range(height):
        l_up_pos=LF_flat+i
        LF.duty(l_up_pos)
        sleep_ms(speed)
      for i in range(height):
        r_up_pos=RF_flat-i
        RF.duty(r_up_pos)
        sleep_ms(speed)
      for i in range(height):
        l_down_pos=l_up_pos-i
        LF.duty(l_down_pos)
        sleep_ms(speed)
      for i in range(height):
        r_down_pos=r_up_pos+i
        RF.duty(r_down_pos)
        sleep_ms(speed)
  if direction == 'left':
    RB.duty(88)
    sleep_ms(20)
    LB.duty(88)
    for i in range(step):  
      for i in range(height):
        r_up_pos=RF_flat-i
        RF.duty(r_up_pos)
        sleep_ms(speed)
      for i in range(height):
        l_up_pos=LF_flat+i
        LF.duty(l_up_pos)
        sleep_ms(speed)
      for i in range(height):
        r_down_pos=r_up_pos+i
        RF.duty(r_down_pos)
        sleep_ms(speed)
      for i in range(height):
        l_down_pos=l_up_pos-i
        LF.duty(l_down_pos)
        sleep_ms(speed)

def tap(direction,n):
  for i in range(n):
    if direction == 'right':
      RF.duty(RF_flat+25)
      sleep_ms(500)
      RF.duty(RF_flat)
      sleep_ms(500)
    elif direction == 'left':
      LF.duty(LF_flat-25)
      sleep_ms(500)
      LF.duty(LF_flat)
      sleep_ms(500)
