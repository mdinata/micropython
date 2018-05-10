#Written by Andi Dinata#May 2018#Under MIT License#visit http://andidinata.com/2017/10/music-dengan-piezo-buzzer/ for the tone table
'''
Here is Happy Birthday Song:
note= ['C3','C3','D3','C3','F3','E3','0',
        'C3','C3','D3','C3','G3','E3','0',
        'C3','C3','C4','A3','F3','F3','E3','D2','0',
        'AS3','AS3','A3','F3','G3','F3']

duration=[0.2,0.2,0.4,0.4,0.4,0.8,0.2,
        0.2,0.2,0.4,0.4,0.4,0.8,0.2,
        0.2,0.2,0.4,0.4,0.2,0.2,0.4,0.4,0.4,
        0.2,0.2,0.4,0.4,0.4,0.4]
'''
from uGPIO import GPIOimport utimetone={"0":"0",
  "C2":"65",	"CS2":"69",	"D2":"73",	"DS2":"78",	"E2":"84",	"F2":"89",	"FS2":"93",	"G2":"101",	"GS2":"104",	"A2":"110",	"AS2":"117",	"B2":"125",	"C3":"131",	"CS3":"139",	"D3":"147",	"DS3":"156",	"E3":"168",	"F3":"175",	"FS3":"185",	"G3":"196",	"GS3":"208",	"A3":"220",	"AS3":"236",	"B3":"247",	"C4":"262"}class Music():    def __init__(self,pin,pin_led=2):        self.pin = GPIO(pin)        self.led = GPIO(pin_led)    def output(self,pitch,duration):        if(pitch==0):            utime.sleep(duration)            return        period = 1.0/pitch        delay = period/2        cycles=int(duration * pitch)        self.led.on()        self.pin.repeat(cycles,delay)        self.led.off()    def play(self,note,duration):        x = 0
        tone_list=[]
        for i in note:
            tone_list.append(int(tone[i]))
        print(tone_list)

        for p in tone_list:            self.output(p,duration[x])            utime.sleep(duration[x]*0.5)            x += 1