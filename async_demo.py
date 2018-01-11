#Written by Andi Dinata
#Under MIT License
#January 2018
#Use the uasyncio library developed by github.com/peterhinch

from uGPIO import GPIO
import uasyncio as asyncio
loop = asyncio.get_event_loop()

class RGB():
    def __init__(self,r=15,g=12,b=13):
        self.blue=GPIO(b,1)
        self.green=GPIO(g,1)
        self.red=GPIO(r,1)
        
    async def fade(self,object,t,s):
        while True:
            for i in range(1,100,s):
                object.scale(i)
                await asyncio.sleep_ms(30)
            await asyncio.sleep(t)
            for i in range(1,100,s):
                object.scale(100-i)
                await asyncio.sleep_ms(30)
            await asyncio.sleep(t)
        
    def off(self):
        self.blue.scale(0)
        self.red.scale(0)
        self.green.scale(0)
    
    def rainbow(self):
        try:
            loop.create_task(self.fade(self.blue,0.3,5))
            loop.create_task(self.fade(self.red,0.5,5))
            loop.create_task(self.fade(self.green,1,5))
            loop.run_forever()
        except KeyboardInterrupt:
            loop.close()
            self.off()
            
    def disco(self):
        try:
            loop.create_task(self.fade(self.blue,0.3,49))
            loop.create_task(self.fade(self.red,0.5,49))
            loop.create_task(self.fade(self.green,1,49))
            loop.run_forever()
        except KeyboardInterrupt:
            loop.close()
            self.off()
