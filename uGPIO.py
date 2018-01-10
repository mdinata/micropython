# micropython wrapper for generic I/O purposes. For micropython in ESP8266 based board
# written by Andi Dinata
# under MIT License

from machine import Pin, PWM
import time

class GPIO():
	def __init__(self,pin,pulse=0):
		self.pin = pin
		self.pulse = pulse
		if pulse == 0:
			self.pin=Pin(self.pin,Pin.OUT)
			self.pin.value(0)
		elif pulse == 1:
			self.pin=PWM(Pin(self.pin),Pin.OUT)
			self.pin.freq(500)
               
        def on(self):
                self.pin.value(1)

        def off(self):
                self.pin.value(0)

        def toggle(self):
		self.pin.value(not self.pin.value())

	def repeat(self,n,t=0.5):
		for i in range(n):
			self.toggle()
			time.sleep(t)
		self.off()

	def scale(self,n):
                if n > 100:
                        n = 100
                elif n < 0:
                        n = 0
                percent = n*10
		self.pin.duty(percent)
		return (percent)

	def fade_in(self,step=5,t=0.1):
                for i in range(0,100,step):
                        self.scale(i)
                        time.sleep(t)
        def fade_out(self,step=5, t=0.1):
                for i in range(0,100,step):
                        self.scale(100-i)
                        time.sleep(t)
                self.scale(0)

        def help():
                print("")
                print("Cheat Sheet Wemos D1 Mini")
                print("-------------------------")
                print("                   ____________")
                print("                  /            |")
                print("             RST-|         =   |- TX")
                print("              A0-|   ESP8266   |- RX")
                print("NO PWM GPIO16 D0-|         SCL-|- D1 GPIO5")
                print("       GPIO14 D5-|-SCK     SDA-|- D2 GPIO4")
                print("       GPIO12 D6-|-MISO        |- D3 GPIO0 PullUp")
                print("       GPIO13 D7-|-MOSI        |- D4 GPIO2 PullUp Built-in Led")
                print("PullDn GPIO15 D8-|             |- G")
                print("             3v3-|_____________|- 5V")
                print("")
