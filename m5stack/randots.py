"""
Random Dots
Draw dots with random outline and fill colors and sizes\
30 mins code challenge #1 
Written by Andi Dinata while waiting for letter administration, 9 April 2018
"""

from m5stack import *
from random import choice, randrange

screen_width, screen_height=lcd.winsize()

colors=[lcd.BLACK,
	lcd.NAVY,
	lcd.DARKGREEN,
	lcd.DARKCYAN,
	lcd.MAROON,
	lcd.PURPLE,
	lcd.OLIVE,
	lcd.LIGHTGREY,
	lcd.DARKGREY,
	lcd.BLUE,
	lcd.GREEN,
	lcd.CYAN,
	lcd.RED,
	lcd.MAGENTA,
	lcd.YELLOW,
	lcd.WHITE,
	lcd.ORANGE,
	lcd.GREENYELLOW,
	lcd.PINK ]

def wipe():
	for i in range(0,screen_height):
		lcd.circle(int(screen_width/2),int(screen_height/2),i,lcd.BLACK,lcd.BLACK)
	
buttonB.releasedFor(0.1,wipe)

while True:
	x=randrange(0,screen_width)
	y=randrange(0,screen_height)
	d=randrange(10,100)
	lcd.circle(x,y,d,choice(colors),choice(colors))
	time.sleep_ms(100)

