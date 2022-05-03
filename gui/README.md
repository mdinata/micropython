## Form
Create simple form for all display types using micropython framebuffer

#### Step 1. Initiate your display device
```python
import pcd8544_fb
from machine import Pin, SPI

spi = SPI(1)
spi.init(baudrate=8000000, polarity=0, phase=0)
cs = Pin(2)
dc = Pin(15)
rst = Pin(0)
bl = Pin(16, Pin.OUT, value=0) # backlight on

display = pcd8544_fb.PCD8544_FB(spi, cs, dc, rst)
```
#### Step 2. Import the form library

Form(display,label,x,y,width,height,invert,fill)<br>

```python
from form import *

f1=Form(display,"Volume",0,0,20,10,invert=False,fill=True)
f2=Form(display,"Total ",0,11,20,10,invert=True,fill=True)
f3=Form(display,"/liter",0,22,20,10,invert=False,fill=True)

t1=Textbox(display,"Pertamax",0,34)

display.show()
```
Result:<br>
<img src="https://github.com/mdinata/micropython/blob/master/gui/asset/form_nokia.jpg" alt="drawing" width="400"/>
<img src="https://github.com/mdinata/micropython/blob/master/gui/asset/form_oled.jpg" alt="drawing" width="400"/>

#### Step 3. Modify
Change value
```python
f1.value(100)
f1.value(100,align='right')
display.show()
```
Clear value
```python
f1.clear()
display.show()
```
## Textbox
#### Step 1.Create instances
```python
from form import *

t1=Textbox(display,"Prev",0,39)
t2=Textbox(display,"OK",38,39)
t3=Textbox(display,"Next",64,39)

display.show()
```
<img src="https://github.com/mdinata/micropython/blob/master/gui/asset/File_000.png" alt="drawing" width="400"/>

#### Step 2. Modify
Invert toggle
```python
t1.toggle()
t2.toggle()
t3.toggle()
```
Change value
```python
t1.string="<<"
t1.clear()
t1.draw()
display.show()
```
## Gauge
Initiate display
```python
from machine import Pin, I2C,ADC
import ssd1306
import time
from gauge import Hbar

i2c=I2C(scl=Pin(5), sda=Pin(4), freq=100000)
display=ssd1306.SSD1306_I2C(128,64,i2c)
```
Create instance
```python
cpu=Hbar(display,"CPU :",x=0,y=0,width=20,height=10,c=1,maxread=1024,step=0.1)        
mem=Hbar(display,"RAM :",0,12,30,10,1,1024)
disk=Hbar(display,"Disk:",0,24,35,10,1,1024,step=0.2)
```
Main program
```python

pot=ADC(0)

while True:
    pot_value=pot.read()

    cpu.value(pot_value,uom="%",series=True)
    mem.value(pot_value,uom="MB",series=True)
    disk.value(pot_value,uom="GB",series=True)
    
    time.sleep(0.1)
    display.show()
    
    cpu.clear()
    mem.clear()
    disk.clear()
```
