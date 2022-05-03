#Andi Dinata
#02 May 2022

import font454 as sf
        
class Hbar:
    def __init__(self,buffer,label,x,y,width,height,c,maxread=100,step=0.1):
        self.buffer=buffer
        self.label=label
        self.x=x+len(self.label)*4
        self.y=y
        self.width=width
        self.height=height
        self.c=c
        self.maxread=maxread
        self.step=step
        self.scale=0
        self.margin=2
        self.border=self.buffer.rect(self.x,self.y,self.width,self.height,self.c)
        self.barwidth=0
        self.percent=0
        self.maxwidth=self.width - (2*self.margin)
        self.barheight=self.height - (2*self.margin)
        self.bar=self.buffer.fill_rect(self.x+ self.margin,
                                       self.y + self.margin,
                                       0,self.barheight,self.c)
    
    def value(self,var,uom="%",series=False):
        self.scale=self.maxwidth / self.maxread
        self.barwidth = var * self.scale
        self.percent = int((self.barwidth / self.maxwidth)*100)
        if series:
            if len(str(self.percent)) < 3:
                string="0{}{} ".format(self.percent,uom)
            else:
                string="{}{}".format(self.percent,uom)
            sf.text(self.buffer,string,self.x+self.width+self.margin,self.y+self.margin,1)
        self.draw()
    
    def clear(self):
        self.bar=self.buffer.fill_rect(self.x + self.margin,
                                   self.y + self.margin,
                                   self.maxwidth,self.barheight,not(self.c))
    def draw(self):
        sf.text(self.buffer,self.label,self.x-len(self.label)*4,self.y+self.margin,1)
        
        self.clear()
        self.bar=self.buffer.fill_rect(self.x + self.margin,
                                       self.y + self.margin,
                                       int(self.barwidth),self.barheight,self.c)
