from machine import Pin, SPI
from time import sleep

from canvas import Canvas

# dimension framebuffer
rowBound = 64       # bytearray 'rows' - 64 rows -> 64bits
colBound = 128//8   # 'cols' in each bytearray - 16 bytes -> 128bits

ScreenSize = (128, 160)

""" EXAMPLE WIRING (MCU runs at 3.3V, so use VIN to get 5V)

https://www.ruten.com.tw/item/show?21923637495764
esp8266
        * GND   - 0V
        * VCC   - 5V                    - USB power VIN (not 3V3)
        * V0    - 5V                    - LCD contrast
        * RS    - 5V 
        * RW    - GPIO13 (Cockle pin7)  - SPI MOSI  (esp32s-23)
        * E     - GPIO14 (Cockle pin5)  - SPI Clock (esp32s-18)
        * PSB   - GND                   - Activate SPI
        * RST   - 5V                    - resetDisplay
        * BLA   - 5V                    - Backlight Anode
        * BLK   - GND                   - Backlight Cathode
        
    By default, attempts to wire to Hardware SPI as described at https://docs.micropython.org/en/latest/esp8266/esp8266/quickref.html#hardware-spi-bus
"""
class Screen(Canvas):
    def __init__(self, sck=None, mosi=None, miso=None, spi=None, resetDisplayPin=None, slaveSelectPin=None, baudrate=1800000):

        self._size = ScreenSize
        self.cmdbuf = bytearray(33) # enough for 1 header byte plus 16 graphic bytes encoded as two bytes each
        self.cmdmv = memoryview(self.cmdbuf)
        
        if spi is not None:
            self.spi = spi
        else:
            polarity=0
            phase=0
            if sck or mosi or miso: # any pins are identified - wire up as software SPI
                if not(sck and mosi and miso):
                    raise AssertionError("All SPI pins sck, mosi and miso need to be specified")
                self.spi = SPI(-1, baudrate=baudrate, polarity=polarity, phase=phase, sck=sck, mosi=mosi, miso=miso)
            else:
                self.spi = SPI(1, baudrate=baudrate, polarity=polarity, phase=phase)

        # allocate frame buffer just once, use memoryview-wrapped bytearrays for rows
        self.fbuff = [memoryview(bytearray(colBound)) for rowPos in range(rowBound)]
 
        self.resetDisplayPin = resetDisplayPin
        if self.resetDisplayPin is not None:
            self.resetDisplayPin.init(mode=Pin.OUT)

        self.slaveSelectPin = slaveSelectPin
        if self.slaveSelectPin is not None:
            self.slaveSelectPin.init(mode=Pin.OUT)

        self.set_rotation(0)  # rotate to 0 degrees

        self.config()


    def config(self):
        self.reset()

        self.select(True)

        self.send_flag(0x30)  # basic instruction set
        self.send_flag(0x30)  # repeated
        self.send_flag(0x0C)  # display on

        self.send_flag(0x34)  # enable RE mode
        self.send_flag(0x34)
        self.send_flag(0x36)  # enable graphics display

        self.select(False)

    # slave select surprisingly? is active high +V means active
    def select(self, selected):
        if self.slaveSelectPin:
            self.slaveSelectPin.value( 1 if selected else 0)

    # reset logic untested
    def reset(self):
        if self.resetDisplayPin is not None:
            # pulse active low to reset screen
            self.resetDisplayPin.value(0)
            sleep(0.1)
            self.resetDisplayPin.value(1)

    def set_rotation(self, rot):
        if rot == 0 or rot == 2:
            self.width = 128
            self.height = 64
        elif rot == 1 or rot == 3:
            self.width = 64
            self.height = 128
        self.rot = rot

    def clear_bytes(self, count):
        for pos in range(count):
            self.cmdbuf[pos] = 0

    def send_flag(self, b):
        count = 3
        pos = 0
        while pos < count:
            self.cmdbuf[pos] = 0
            pos += 1
        self.cmdbuf[0] = 0b11111000  # rs = 0
        self.cmdbuf[1] = b & 0xF0
        self.cmdbuf[2] = (b & 0x0F) << 4
        submv = self.cmdmv[:count]
        self.spi.write(submv)
        del submv

    def send_address(self, b1, b2):
        count = 5
        pos = 0
        while pos < count:
            self.cmdbuf[pos] = 0
            pos += 1
        self.cmdbuf[0] = 0b11111000  # rs = 0
        self.cmdbuf[1] = b1 & 0xF0
        self.cmdbuf[2] = (b1 & 0x0F) << 4
        self.cmdbuf[3] = b2 & 0xF0
        self.cmdbuf[4] = (b2 & 0x0F) << 4
        submv = self.cmdmv[:count]
        self.spi.write(submv)
        del submv

    def send_data(self, arr):
        arrlen = len(arr)
        count = 1 + (arrlen << 1)
        pos = 0
        while pos < count:
            self.cmdbuf[pos] = 0
            pos += 1
        self.cmdbuf[0] = 0b11111000 | 0x02  # rs = 1
        pos = 0
        while pos < arrlen: # inlined code from marshal_byte
            self.cmdbuf[1 + (pos << 1)] = arr[pos] & 0xF0
            self.cmdbuf[2 + (pos << 1)] = (arr[pos] & 0x0F) << 4
            pos += 1
        submv = self.cmdmv[:count]
        self.spi.write(submv)
        del submv

    def clear(self):
        rowPos = 0
        while rowPos < rowBound:
            row = self.fbuff[rowPos]
            colPos = 0
            while colPos < colBound:
                row[colPos]=0
                colPos += 1
            rowPos += 1

    def plot(self, x, y, set=True):
        if x<0 or x>=self.width or y<0 or y>=self.height:
            return
        if set:
            if self.rot == 0:
                self.fbuff[y][x // 8] |= 1 << (7 - (x % 8))
            elif self.rot == 1:
                self.fbuff[x][15 - (y // 8)] |= 1 << (y % 8)
            elif self.rot == 2:
                self.fbuff[63 - y][15 - (x // 8)] |= 1 << (x % 8)
            elif self.rot == 3:
                self.fbuff[63 - x][y // 8] |= 1 << (7 - (y % 8))
        else:
            if self.rot == 0:
                self.fbuff[y][x // 8] &= ~(1 << (7 - (x % 8)))
            elif self.rot == 1:
                self.fbuff[x][15 - (y // 8)] &= ~(1 << (y % 8))
            elif self.rot == 2:
                self.fbuff[63 - y][15 - (x // 8)] &= ~(1 << (x % 8))
            elif self.rot == 3:
                self.fbuff[63 - x][y // 8] &= ~(1 << (7 - (y % 8)))


    			
    def redraw(self, dx1=None, dy1=None, dx2=None, dy2=None):
        """
        # TODO CH bug here? (inherited from https://github.com/JMW95/pyST7920 ) buffer address ranges calculated incorrect for (bottom-right?) rectangles
        # TODO CH HACK uncomment 4 lines below for redraw rectangle to be ignored
        dx1 = 0
        dy1 = 0
        dx2 = 127
        dy2 = 63
        """
        # TODO CH consider more efficient bounds checking
        if dx1 is None:
            dx1 = 0
        else:
            dx1 = max(0, dx1)
            dx1 = min(127, dx1)
        if dx2 is None:
            dx2 = 127
        else:
            dx2 = max(0, dx2)
            dx2 = min(127, dx2)
        if dy1 is None:
            dy1 = 0
        else:
            dy1 = max(0, dy1)
            dy1 = min(63, dy1)
        if dy2 is None:
            dy2 = 63
        else:
            dy2 = max(0, dy2)
            dy2 = min(63, dy2)
        try:
            self.select(True)
            i = dy1
            while i < dy2 + 1:
                self.send_address(0x80 + i % 32, 0x80 + ((dx1 // 16) + (8 if i >= 32 else 0)))
                self.send_data(self.fbuff[i][dx1 // 16:(dx2 // 8) + 1])
                i+=1
        finally:
            self.select(False)
