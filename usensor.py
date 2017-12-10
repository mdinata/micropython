from machine import Pin, PWM
import time

class Ultrasonic():
    def __init__(self,trig_pin,echo_pin):
        self.trig_pin = trig_pin
        self.echo_pin = echo_pin
        self.trig = Pin(self.trig_pin, Pin.OUT)
        self.trig.off()
        time.sleep_ms(2)
        self.trig.on()
        time.sleep_ms(10)
        self.trig.off()

        self.echo = Pin(self.echo_pin, Pin.IN)

    def get_distance(self,unit="cm"):
        self.trig.on()
        time.sleep_ms(10)
        self.trig.off()

        while self.echo.value() == 0:
            pass
        start = time.ticks_us()

        while self.echo.value() == 1:
            pass
        stop = time.ticks_us()
        d = (stop - start) / 58
        distance = round(d,2)
        if unit == "mm":
            factor = 10
        elif unit == "cm":
            factor = 1
        elif unit == "m":
            factor = 0.01
            
        return distance*factor
        
    def get_average(self,n=3,unit="cm"):
        d=[]
        for i in range(n):
            d.insert(0,self.get_distance(unit))
            time.sleep_ms(100)
        print(d)
        return sum(d)/n
