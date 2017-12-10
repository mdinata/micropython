# micropython GPIO wrapper for ESP8266 based board
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

	def repeat(self,n,t=0.5):
		for i in range(n):
			self.pin.value(1)
			time.sleep(t)
			self.pin.value(0)
			time.sleep(t)

	def scale(self,n):
                if n > 100:
                        n = 100
                elif n < 0:
                        n = 0
                percent = n*10
		self.pin.duty(percent)
                        

        def help():
                print("Cheat Sheet")
                print("---------------------------------------")
                print("D0 IO                           GPIO16")
                print("D1 IO SCL                       GPIO5")
                print("D2 IO SDA                       GPIO4")
                print("D3 IO 10k Pull Up               GPIO0")
                print("D4 IO 10k Pull Up, Built-in Led GPIO2")
                print("D5 IO SCK                       GPIO14")
                print("D6 IO MISO                      GPIO12")
                print("D7 IO MOSI                      GPIO13")
                print("D8 IO 10k Pull Down             GPIO15")
                print("All Pins have PWM except D0")

