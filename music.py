#Written by Andi Dinata
#January 2018
#Under MIT License
#visit http://andidinata.com/2017/10/music-dengan-piezo-buzzer/ for the tone table

from uGPIO import GPIO
import utime

class Music():
    def __init__(self,pin,pin_led=2):
        self.pin = GPIO(pin)
        self.led = GPIO(pin_led)

    def output(self,pitch,duration):
        if(pitch==0):
            utime.sleep(duration)
            return
        period = 1.0/pitch
        delay = period/2
        cycles=int(duration * pitch)
        self.led.on()
        self.pin.repeat(cycles,delay)
        self.led.off()

    def play(self,song):
        x = 0
        if song ==1:
            print("Playing Happy Birthday...")
            pitch= [131,131,147,131,175,168,0,
                    131,131,147,131,196,168,0,
                    131,131,262,220,175,175,168,147,0,
                    236,236,220,175,196,175]
            duration=[0.2,0.2,0.4,0.4,0.4,0.8,0.2,
                    0.2,0.2,0.4,0.4,0.4,0.8,0.2,
                    0.2,0.2,0.4,0.4,0.2,0.2,0.4,0.4,0.4,
                    0.2,0.2,0.4,0.4,0.4,0.4]
        for p in pitch:
            self.output(p,duration[x])
            utime.sleep(duration[x]*0.5)
            x += 1
            

