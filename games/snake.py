'''
Micropython Game for Beginners: Snake
written by Andi Dinata June 2018
Step-by-step explanation
Python skill required:
1. Importing libraries
2. list operations
3. if statements
4. simple arithmatics
5. Hardware interaction (SPI ledmatrix and buttons)
'''

#1. Import libraries we need
import max7219
from machine import Pin, SPI,freq, reset
import utime
import urandom
import number

#2. Initialize the hardware.
## Bring ESP8266 to maximum speed 160MHz
freq(160000000)
## Initialize the led matrix 8x8
spi=SPI(1, baudrate=10000000, polarity=0, phase=0)
device=max7219.Matrix8x8(spi, Pin(2), 1)
## Start the display
device.fill(0)
device.brightness(10)
utime.sleep(0.1)
device.show()
## Setup all directional buttons
s1 = Pin(5, Pin.IN, Pin.PULL_UP) #left
s2 = Pin(0, Pin.IN, Pin.PULL_UP) #up
s3 = Pin(4, Pin.IN, Pin.PULL_UP) #down
s4 = Pin(3, Pin.IN, Pin.PULL_UP) #right

#3. Let's get started
## This is our snake, located at coordinate x,y at (2,2)
snake=[(2,2)]
## Snake needs to move and has direction. For start the snake does not make any move, so it stays or zero movement (0,0)
## As we need to keep track the snake movement, we need the movement data accessible anywhere, so we make it global variable
global snake_dir
snake_dir=(0,0)
## Here is the trick, when the snake moves, we need to know if snake has made a movement, flag = 1 move, flag = 0 no move.
global flag
flag=0
## Snake will find food, this is the basket of the food, empty basket.
food=[]

## This is a trick needed for the 5th part of main program
tail_list=[]

## What happen when the game is over condition said in 6th part of main program. When game over, the length of snake is the score.
#   How long can you go?
def game_over():
    device.fill(0)
    device.show()
    utime.sleep(0.5)
    number.draw(len(snake))
    utime.sleep(2)
    reset()

#4. Now we are in the main program, starting with while True statements, which will loop all the scripts forever until
#   a condition reach to quit    
while True:
##  1st part of main program is to tell the snake how to move when the button is clicked
    if s3.value()==0:
        snake_dir=(1,0)
	utime.sleep(0.05)
	flag=1
    elif s2.value() ==0:
	snake_dir=(-1,0)
	utime.sleep(0.05)
	flag=1
    elif s4.value() ==0:
	snake_dir=(0,-1)
	utime.sleep(0.05)
	flag=1
    elif s1.value() ==0: 
	snake_dir=(0,1)
	utime.sleep(0.05)
	flag=1
	
## 2nd part of the program is about how to spawn the food randomly. And the food remains dsplayed until gets eaten
    r=urandom.getrandbits(3)
    if r ==0:
        x,y = urandom.getrandbits(3),urandom.getrandbits(3)
        food.append((x,y))
        
## 3rd part is what happens when the food is eaten by the snake. Is when the snake head hits the food location
    (hx,hy)=snake[0]
    if len(food)>0:
        for x,y in food:
            device.pixel(x,y,1)
            device.show()
## When the snake head hits the food, then the food will make the snake longer
            if hx==x and hy==y:
                snake.append((x,y))
                food.remove((x,y))
                for x,y in food:
                    device.pixel(x,y,0)
                    device.show()
                    
## 4th part is to create a wormhole. Wormhole means, the snake can go from one edge to another edge by just passing through it		
    x=hx+snake_dir[0]
    y=hy+snake_dir[1]

    if x > 7:
            x = 0
    if x < 0:
            x = 7
    if y > 7:
            y = 0
    if y < 0:
            y = 7
            
    snake.insert(0,(x,y))

    for x,y in snake:
        device.pixel(x,y,1)
        device.show()
    
    utime.sleep(0.3)
    
## 5th part is a trick. When the snake move, it has to move entirely, leaving no trace. this trick will erase the trace of snake
#    movement

    length=len(snake)
    tail=snake[length-1]
    
    tail_list.insert(0,tail)
    for x,y in tail_list:
        device.pixel(x,y,0)
        device.show()

    tail_list=[]

    flag=0
    snake.pop()

## 6th part is collision check. This when the snake hits any part of its body then we will call for game over
    if snake.count(snake[0]) > 1:
        game_over()
        


