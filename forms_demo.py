from forms import *

f1=Form("Volume",0,0,20,10,invert=False,fill=True)
f2=Form("Total ",0,11,20,10,invert=True,fill=True)
f3=Form("/liter",0,22,20,10,invert=False,fill=True)

t1=Textbox("MAX",0,34)
t2=Textbox("LITE",20,34)
t3=Textbox("DEX",44,34)

def presst1(arg):
    t1.toggle()

def presst2(arg):
    t2.toggle()
    
def presst3(arg):
    t3.toggle()

    
btn1=Pin(5, Pin.IN, Pin.PULL_UP)
btn2=Pin(4, Pin.IN, Pin.PULL_UP)
btn3=Pin(12, Pin.IN, Pin.PULL_UP)

btn1.irq(handler=presst1,trigger=Pin.IRQ_FALLING)
btn2.irq(handler=presst2,trigger=Pin.IRQ_FALLING)
btn3.irq(handler=presst3,trigger=Pin.IRQ_FALLING)

display.show()