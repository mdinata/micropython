'''
Nokia 5110 Micropython Simulator
Andi Dinata 7 September 2021
'''

from turtle import *

class Nokia():
    def __init__(self,x=-250,y=80,font_height=32):
        setup(700,700)
        tracer(0,0)
        bgpic('/usr/lib/python3.7/nokia_bg.gif')
        self.x=x
        self.y=y
        self.font_height=font_height
        self.t=Turtle()
        self.t.hideturtle()
        
    def _offset(self,posx,posy,down=False):
        self.t.penup()
        
        if down is True:
            self.t.pendown()
        
        self.t.goto(self.x+posx,self.y-posy)
        
        return (self.t.xcor(),self.t.ycor())
    
    def _color(self,colorstr):
        if colorstr == 1:
            self.t.pencolor("black")
        else:
            self.t.pencolor("white")

    def text(self,string,posx,posy,color=1):
        repos_x,repos_y=self._offset(posx,posy)
        
        self.t.goto(self.x+(6*posx),self.y-(6*posy)-self.font_height)
        self._color(color)
        self.t.write((posx,posy))
        self.t.write(string,font=("Arial",self.font_height,"bold"))
        
    
#         self.t.stamp()
    
    def show(self):
        update()
    
    def hline(self,posx,posy,width,color=1,size=5):
        self.t.penup()
        self._offset(posx,posy)
        self._color(color)
        self.t.goto(self.x+posx,self.y-(6*posy))
        self.t.write((posx,posy))
        self.t.pensize(size)
        self.t.pendown()
        self.t.forward(width*6)
        self.t.penup()
#         self.t.stamp()
    
    def vline(self,posx,posy,width,color=1,size=5):
        self.t.setheading(270)
        self.t.penup()
        self._offset(posx,posy)
        self._color(color)
        self.t.goto(self.x+(6*posx),self.y)
        self.t.write((posx,posy))
        self.t.pensize(size)
        self.t.pendown()
        self.t.forward(width*6)
        self.t.penup()
#         self.t.stamp()
        
    def rect(self,posx,posy,width,height,color=1):
        self._offset(posx,posy)
        self._color(color)
        self.t.goto(self.x+(6*+posx),self.y-(6*posy))
        self.t.write((posx,posy))
        self.t.pendown()
        self.t.pensize(4)
        for i in range(2):
            self.t.forward(width*6)
            self.t.right(90)
            self.t.forward(height*6)
            self.t.right(90)
        self.t.penup()
#         self.t.stamp()
    
    def fill_rect(self,posx,posy,width,height,color=1,fill='black'):
        self._offset(posx,posy)
        self._color(color)
        self.t.goto(self.x+(6*posx),self.y-(6*posy))
        self.t.write((posx,posy))
        self.t.pendown()
        self.t.pensize(4)
        if color == 0:
            fill='white'
        self.t.fillcolor(fill)
        self.t.begin_fill()
        for i in range(2):
            self.t.forward(width*6)
            self.t.right(90)
            self.t.forward(height*6)
            self.t.right(90)
        self.t.end_fill()
        self.t.penup()
#         self.t.stamp()
    
    def pixel(self,posx,posy,color):
        self._offset(posx,posy)
        self._color(color)
        self.t.goto(self.x+(6*posx),self.y-(6*posy))
        self.t.dot()
#         self.t.stamp()

    def line(self,posx0,posy0,posx1,posy1,color):
        self._offset(posx0,posy0)
        self._color(color)
        self.t.pensize(4)
        
        self.t.goto(self.x+(6*posx0),self.y-(6*posy0))
        
        self._offset(posx1,posy1,down=True)
        self.t.goto(self.x+(6*posx1),self.y-(6*posy1))

        self.t.penup()
        #self.t.stamp()
    
    
    def fill(self,num):
        if num == 0:
            self.t.clear()
            update()
            
    def picture(self,posx,posy,filename):
        with open(filename,'r') as f:
            pic_bin=f.read()
            pic_list=pic_bin.split('\n')
            for y, row in enumerate(pic_list):
                for x in enumerate(row):
                    self.pixel(x[0]+posx,y+posy,int(x[1]))
        f.close()

class Button():
    def __init__(self,posx,posy,sh='circle',direction=0,c='black',val=1):
        self.b=Turtle()
        self.b.penup()
        self.b.goto(posx,posy)
        self.b.pendown()
        self.c=c
        self.b.color(self.c)
        self.b.setheading(direction)
        self.b.shape(sh)
        self.b.shapesize(3)
        self.b.onclick(self.pressed,1)
        self.b.onrelease(self.released,1)
        self.val=val
        update()
#         self.b.write(label,align="center",font=("Arial",10,"bold"))
    
    def value(self):
        return self.val
    
    def pressed(self,x,y):
        self.b.color('grey')
        self.val=0
        print("button ",self.c," clicked", self.val)
        update()
        
    def released(self,x,y):
        self.b.color(self.c)
        self.val=1
        print("button ",self.c," released", self.val)
        update()
    
    
if __name__ == '__main__':
    display=Nokia()
    up=Button(-250,-300,sh='triangle',direction=90,c='cyan')
    down=Button(-180,-280,sh='triangle',direction=270,c='magenta')
    left=Button(-110,-285,sh='triangle',direction=180,c='yellow')
    right=Button(-40,-285,sh='triangle',direction=0,c='green')
    ok=Button(250,-290,sh='circle',direction=0,c='red')

    
    update()
    
    import time
    
    dx=0
    dy=0
    
    while True:
        if up.value() == 0:
            display.fill(0)
            dy -= 1            
        if down.value() == 0:
            display.fill(0)
            dy += 1
        if left.value() == 0:
            display.fill(0)
            dx -= 1
        if right.value() == 0:
            display.fill(0)
            dx += 1
        if ok.value ==0:
            pass
        
        display.rect(20+dx,20+dy,20,20,1)
        update()
        time.sleep(0.1)
#     import os
#     os.chdir('/home/colab/Colab/_graphics')
#     display.picture(0,0,'logo_starbucks.txt')
#     display.pixel(0,0,1)
#     display.line(0,0,84,48,1)
#     display.line(0,48,24,24,1) #buggy 
#     display.rect(0,0,20,20,1)
# #     display.vline(84,0,48,1)
#     display.text("1234567890",0,0,1)
#     display.text("123456789012345678901",0,8,1)
#     for i in range(6):
#         display.hline(0,i*8,84,1)
        
