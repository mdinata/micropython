## Convert JPG to Binary
1. Use GIMP/Photoshop to convert the image to indexed color (1-bit)
2. go to (https://www.dcode.fr/binary-image) to binarize the image. Choose with custom resolution. Put 84 or 48 according to the Nokia 5110 pixel length or width then click convert
3. download as txt file to your local disk and rename the file to something meaningful

## Load the txt to micropython
Use ampy or uPyCraft or any IDE to load txt in the usual way. Here is example on ampy
```sh
ampy -b 115200 -p /dev/ttyUSB0 put image.txt
```
## Usage Nokia 5110.py
Inside Micropython, Write the syntax without prompt sign
```py
>>> from nokia5110 import Display
>>> lcd=Display()
>>> lcd.picture(0,0,"image.txt")
```
