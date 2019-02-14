# Andi Dinata
# 15 February 2019
# get pcd8544.py from https://github.com/mcauser/micropython-pcd8544

import pcd8544, framebuf
from machine import Pin, SPI

class Display:
    def __init__(self):
        self.spi = SPI(1)
        self.spi.init(baudrate=8000000, polarity=0, phase=0)
        self.cs = Pin(2)
        self.dc = Pin(15)
        self.rst = Pin(0)
        self.bl = Pin(12, Pin.OUT)
        self.lcd = pcd8544.PCD8544(self.spi, self.cs, self.dc, self.rst)
        self.buffer = bytearray((self.lcd.height // 8) * self.lcd.width)
        self.framebuf = framebuf.FrameBuffer1(self.buffer, self.lcd.width, self.lcd.height)
        
    def on(self):
        self.bl.value(1)
    
    def off(self):
        self.bl.value(0)
        
    def fill(self,color,now=1):
        self.framebuf.fill(color)
        if now ==1:
          self.lcd.data(self.buffer)
    
    def text(self,string,pos_x,pos_y,color,now=1):
        self.framebuf.text(string,pos_x,pos_y,color)
        if now ==1:  
          self.lcd.data(self.buffer)

    def pixel(self,pos_x,pos_y,color,now=1):
        self.framebuf.pixel(pos_x,pos_y,color)
        if now ==1:  
          self.lcd.data(self.buffer)
      
    def line(self,pos_x1,pos_y1,pos_x2,pos_y2,color,now=1):
        self.framebuf.line(pos_x1,pos_y1,pos_x2,pos_y2,color)
        if now ==1:
          self.lcd.data(self.buffer)
  
    def hline(self,pos_x,pos_y,width,color,now=1):
        self.framebuf.hline(pos_x,pos_y,width,color)
        if now ==1:
          self.lcd.data(self.buffer)
  
    def vline(self,pos_x,pos_y,width,color,now=1):
        self.framebuf.vline(pos_x,pos_y,width,color)
        if now ==1:
          self.lcd.data(self.buffer)

    def rectangle(self,pos_x,pos_y,width,length,color,now=1):
        self.framebuf.rect(pos_x,pos_y,width,length,color)
        if now ==1:
          self.lcd.data(self.buffer)

    def rectangle_fill(self,pos_x,pos_y,width,length,color,now=1):
        self.framebuf.fill_rect(pos_x,pos_y,width,length,color)
        if now ==1:
          self.lcd.data(self.buffer)

    def clear(self):
        self.lcd.clear()

    def image(self,data):
        self.lcd.data(bytearray(data))
  
    def picture(self,pos_x,pos_y,filename):
        file=open(filename,'r')
        pic_bin=file.read()
        pic_list=pic_bin.split('\r\n')
        for y, row in enumerate(pic_list):
            for x in enumerate(row):
                self.framebuf.pixel(x[0]+pos_x,y+pos_y,int(x[1]))
        self.lcd.data(self.buffer)
        file.close()
        
    def picture_invert(self,pos_x,pos_y,filename):
        file=open(filename,'r')
        pic_bin=file.read()
        pic_list=pic_bin.split('\r\n')
        for y, row in enumerate(pic_list):
            for x in enumerate(row):
                color = x[1]
                if color == '1':
                    color = 0
                if color == '0':
                    color = 1
                self.framebuf.pixel(x[0]+pos_x,y+pos_y,color)
        self.lcd.data(self.buffer)
        file.close()
    
