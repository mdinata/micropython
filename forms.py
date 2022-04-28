import pcd8544_fb
from machine import Pin, SPI, ADC
import font454 as sf
import time

spi = SPI(1)
spi.init(baudrate=8000000, polarity=0, phase=0)
cs = Pin(2)
dc = Pin(15)
rst = Pin(0)
bl = Pin(16, Pin.OUT, value=1) # backlight on

display = pcd8544_fb.PCD8544_FB(spi, cs, dc, rst)

class Form:
    def __init__(self,string,x,y,width,height,invert=False,fill=False):
        self.string=string+":"
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.margin=(self.height-5)//2
        self.invert=invert
        self.fill=fill
        self.label()
        self.box()
           
    def label(self,c=1):
        sf.text(display,self.string,self.x+self.margin,self.y+self.margin,c)
        
    def box(self,c=1):
        if self.fill:
            self.width=display.width-((len(self.string)*4)+self.margin)
        
        if self.invert:
            display.fill_rect(len(self.string)*4+self.margin,self.y,self.width,self.height,c)
        else:
            display.rect(len(self.string)*4+self.margin,self.y,self.width,self.height,c)
    
    def value(self,valuestring,c=1,align='left'):
        if align == 'left':
            x=(len(self.string)*4)+self.margin*2
        elif align == 'right':
            x=display.width-(len(valuestring)*4)-self.margin
        
        if self.invert:
            foreground,background=not(c),c
        else:
            foreground,background=c,not(c)
        
        sf.text(display,valuestring,x,(self.y+self.margin),foreground,background)
    
    def clear(self,c=1):
        if self.fill:
            self.width=display.width-((len(self.string)*4)+self.margin)
        
        if self.invert:
            display.fill_rect(len(self.string)*4+self.margin,self.y,self.width,self.height,c)
        else:
            display.fill_rect(len(self.string)*4+self.margin,self.y,self.width,self.height,not(c))
            display.rect(len(self.string)*4+self.margin,self.y,self.width,self.height,c)

class Textbox:
    def __init__(self,string,x,y,invert=False):
        self.string=string
        self.x=x
        self.y=y
        self.margin=2
        self.width = ((len(self.string))*4)+(2*self.margin)
        self.height=5 + 2*(self.margin)
        self.invert=invert
        self.draw()
            
    def draw(self,c=1):
        if self.invert:
            display.fill_rect(self.x,self.y,self.width,self.height,c)
            sf.text(display,self.string,self.x+self.margin, self.y+self.margin,not(c),c)
        else:
            display.rect(self.x,self.y,self.width,self.height,c)
            sf.text(display,self.string,self.x+self.margin, self.y+self.margin,c)
    
    def clear(self,c=1):        
        if self.invert:
            display.fill_rect(self.x,self.y,self.width,self.height,c)
        else:
            display.fill_rect(self.x,self.y,self.width,self.height,not(c))
            display.rect(self.x,self.y,self.width,self.height,c)
        self.draw()
        display.show()

    def toggle(self):
        self.invert=not(self.invert)
        print(self.invert)
        self.draw()
        display.show()
        self.clear()
         
if __name__ == '__main__':
    pot=ADC(0)
    
    f1=Form("Volume",0,0,20,10,invert=False,fill=True)
    f2=Form("Total ",0,11,20,10,invert=True,fill=True)
    f3=Form("/liter",0,22,20,10,invert=False,fill=True)
    
    t1=Textbox("Pertamax",0,34)
     
    while True:
        val=pot.read() // 10.2
        
        f1.clear()
        f1.value(str(int(val)),align='right')
        f2.clear()
        f2.value("{:,}".format(int(val*12500)),align='right')
        f3.value("12500",align='right')
        
        time.sleep(0.1)
        display.show()