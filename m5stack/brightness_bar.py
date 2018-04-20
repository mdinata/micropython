"""
Screen Brightness
Adjust screen brightness bar
on the go coding challenge #2 while on taxi from hotel to office Thu, 19 April 2018
by Andi Dinata
"""

from m5stack import *

n =0
max = 10

lcd.clear()
lcd.font(lcd.FONT_Comic)
lcd.text(lcd.CENTER,30,"Screen Brightness",lcd.WHITE)
lcd.font(lcd.FONT_7seg)

def more():
	global n
	n = n + 1
	brightness(n)
	
def less():
	global n
	n=n-1
	brightness(n)	

def brightness(n):
	if n <= max:
		lcd.setBrightness(100*n)
		lcd.rect(20,120,280,30,lcd.WHITE,lcd.BLACK)
		lcd.rect(20,120,(28*n),30,lcd.WHITE,lcd.YELLOW)
		lcd.textClear(lcd.CENTER,70,str(10*n),lcd.WHITE)
		lcd.text(lcd.CENTER,70,str(10*n),lcd.WHITE)
	
buttonA.releasedFor(0.05,less)
buttonC.releasedFor(0.05,more)
