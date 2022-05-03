#Andi Dinata
#01 May 2022

import font454 as sf

class Form:
    def __init__(self,buffer,string,x,y,width,height,invert=False,fill=False):
        self.buffer=buffer
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
        sf.text(self.buffer,self.string,self.x+self.margin,self.y+self.margin,c)
        
    def box(self,c=1):
        if self.fill:
            self.width=self.buffer.width-((len(self.string)*4)+self.margin)
        
        if self.invert:
            self.buffer.fill_rect(len(self.string)*4+self.margin,self.y,self.width,self.height,c)
        else:
            self.buffer.rect(len(self.string)*4+self.margin,self.y,self.width,self.height,c)
    
    def value(self,valuestring,c=1,align='left'):
        if isinstance(valuestring,int) or isinstance(valuestring,float):
            valuestring=str(valuestring)
            
        if align == 'left':
            x=(len(self.string)*4)+self.margin*2
        elif align == 'right':
            x=self.buffer.width-(len(valuestring)*4)-self.margin
        
        if self.invert:
            foreground,background=not(c),c
        else:
            foreground,background=c,not(c)
        
        sf.text(self.buffer,valuestring,x,(self.y+self.margin),foreground,background)
    
    def clear(self,c=1):
        if self.fill:
            self.width=self.buffer.width-((len(self.string)*4)+self.margin)
        
        if self.invert:
            self.buffer.fill_rect(len(self.string)*4+self.margin,self.y,self.width,self.height,c)
        else:
            self.buffer.fill_rect(len(self.string)*4+self.margin,self.y,self.width,self.height,not(c))
            self.buffer.rect(len(self.string)*4+self.margin,self.y,self.width,self.height,c)

class Textbox:
    def __init__(self,buffer,string,x,y,invert=False):
        self.buffer=buffer
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
            self.buffer.fill_rect(self.x,self.y,self.width,self.height,c)
            sf.text(self.buffer,self.string,self.x+self.margin, self.y+self.margin,not(c),c)
        else:
            self.buffer.rect(self.x,self.y,self.width,self.height,c)
            sf.text(self.buffer,self.string,self.x+self.margin, self.y+self.margin,c)
    
    def clear(self,c=1):        
        if self.invert:
            self.buffer.fill_rect(self.x,self.y,self.width,self.height,c)
        else:
            self.buffer.fill_rect(self.x,self.y,self.width,self.height,not(c))
            self.buffer.rect(self.x,self.y,self.width,self.height,c)
        self.draw()
        self.buffer.show()

    def toggle(self):
        self.invert=not(self.invert)
        print(self.invert)
        self.draw()
        self.buffer.show()
        self.clear()
