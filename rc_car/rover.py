#2 DC Motor Controller with NodeMCU Motor Shield
#Written by Andi Dinata
#January 2018
#Under MIT License

from machine import Pin, PWM
import time

class Motor():
  def __init__(self, pin_motorA=5, pin_directionA=0, pin_motorB=4, pin_directionB=2):
    #Motor A, right side
    self.pin_motorA=PWM(Pin(pin_motorA),Pin.OUT)
    self.pin_motorA.freq(500)
    self.pin_directionA=Pin(pin_directionA, Pin.OUT)
       
    #Motor B, left side
    self.pin_motorB=PWM(Pin(pin_motorB),Pin.OUT)
    self.pin_motorB.freq(500)
    self.pin_directionB=Pin(pin_directionB, Pin.OUT)
    
  def forward(self,motorID,speed=500):
    if motorID == 1:
      self.pin_directionA.value(1)
      self.pin_motorA.duty(speed)
      print("kanan maju")
    elif motorID == 2:
      self.pin_directionB.value(1)
      self.pin_motorB.duty(speed)
      print("kiri maju")
      
  def reverse(self,motorID):
    if motorID == 1:
      self.pin_directionA.value(0)
    elif motorID == 2:
      self.pin_directionB.value(0)
    
  def stop(self, motorID):
    if motorID == 1:
      self.pin_motorA.duty(0)
    elif motorID == 2:
      self.pin_motorB.duty(0)
    else:
      self.pin_motorA.duty(0)
      self.pin_motorB.duty(0)
  
  def move(self,speed=500,direction=1,factor=0):
    self.pin_directionA.value(direction)
    self.pin_directionB.value(direction)
    self.pin_motorA.duty(speed+factor)
    self.pin_motorB.duty(speed+factor)
    return speed
  
  def turn(self,side="left",duration=0.5,direction=1):
    moving_speed=self.move()
    print('moving speed=',moving_speed)
    self.pin_directionA.value(direction)
    self.pin_directionB.value(direction)
    if side == "right":
      self.pin_motorA.duty(0)
      self.pin_motorB.duty(moving_speed)
      time.sleep(duration)
    elif side == "left":
      self.pin_motorA.duty(moving_speed)
      self.pin_motorB.duty(0)
      time.sleep(duration)
    else:
      pass

    self.pin_motorA.duty(moving_speed)
    self.pin_motorB.duty(moving_speed)
  
  def pivot(self,duration=0.5):
    self.pin_motorA.duty(0)
    self.pin_motorB.duty(0)
    self.pin_directionA.value(0)
    self.pin_motorA.duty(500)
    self.pin_motorB.duty(500)
    time.sleep(duration)
    self.pin_motorA.duty(0)
    self.pin_motorB.duty(0)

  def gear(self,gear=2):
    if gear == 1:
        self.pin_motorA.duty(250)
        self.pin_motorB.duty(250)
    elif gear == 2:
        self.pin_motorA.duty(500)
        self.pin_motorB.duty(500)
    elif gear == 3:
        self.pin_motorA.duty(1000)
        self.pin_motorB.duty(1000)
    


