#Led Matrix 8x8 Simulator
#Andi Dinata 2021
#MIT License

import turtle
from bitmapfont import *

turtle.tracer(0,0)
turtle.bgcolor('white')

class Matrix():
    def __init__(self,column,row,c=1,pixel_size=70,coord=list()):
        self.column=column
        self.row=row
        self.c=c
        self.space=pixel_size
        self.t=turtle.Turtle()
        self.t.penup()
        self.coord=[]
        self.fill(0)
        self.f=BitmapFont(self.column*self.row,8,self.pixel)
        self.f.init()
        turtle.title("LED MATRIX {}X{} SIMULATION".format(self.column,self.row))
        turtle.setup((self.column/8)*self.space*10,self.space*10)
        turtle.update()
        
    def dots(self,posx,posy,c):
        self.t.goto(posx-(250*(self.column/8)*self.space/70),-posy+(250*self.space/70))
        self.t.dot(self.space,c)

    def pixel(self,x,y,on=1):
        self.t.hideturtle()
        if on == 0 and (x,y) in self.coord:
            self.coord.remove((x,y))
        else:
            self.coord.append((x,y))
        self.c = on
        
    def show(self):
        self.t.clear()
        for row in range(self.row):
            for col in range(self.column):
                if (col,row) in self.coord:
                    self.c='red'
                else:
                    self.c='black'
                                        
                self.dots(col*(self.space+1),row*(self.space+1),self.c)
                
        turtle.update()
        
    def hline(self,x,y,length,c):
        for i in range(length):
            self.pixel(x+i,y,c)

    def vline(self,x,y,length,c):
        for i in range(length):
            self.pixel(x,y+i,c)
        
    def rect(self, x0, y0, width, height, *args, **kwargs):
        self.hline(x0, y0, width, *args, **kwargs)
        self.hline(x0, y0+height-1, width, *args, **kwargs)
        self.vline(x0, y0, height, *args, **kwargs)
        self.vline(x0+width-1, y0, height, *args, **kwargs)
    
    def fill_rect(self, x0, y0, width, height, *args, **kwargs):
        for i in range(x0, x0+width):
            self.vline(i, y0, height, *args, **kwargs)

    def fill(self,on):
        self.coord=[]
    
    def scroll_left(self,string,delay=0.05):
        for c in range(len(string)*8):
            self.fill(0)
            self.f.text(string,-c,0)
            self.show()
            time.sleep(delay)         

    def draw(self,matrix):
        self.fill(0)
        for y,row in enumerate(matrix):
            for x in enumerate(row):
                self.pixel(x[0],y,x[1])
    
    def legend(self,posx):
        self.t.showturtle()
        self.t.goto(posx-(250*(self.column/8)*self.space/70),-posy+(250*self.space/70))

if __name__ == '__main__':
    import time
    display=Matrix(column=8,row=8,pixel_size=40)
    display.show()