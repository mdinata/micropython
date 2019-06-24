# Micropython ESP8266 LED MATRIX
# It is non-blocking server
# Micropython is Cool'
# Andi Dinata
# June 2019
# MIT License

import max7219
from machine import Pin, SPI,freq
import time

tile=4
freq(160000000)
spi=SPI(1, baudrate=10000000, polarity=0, phase=0)
device=max7219.Matrix8x8(spi, Pin(2), tile)
device.brightness(3)
device.fill(0)
device.show()

html = """<!DOCTYPE html>
<html>
<head><title>ESP8266 Led Matrix</title> <link rel="icon" href="data:,"> </head>
<meta content='width=device-width; initial-scale=1.8; maximum-scale=1.8; minimum-scale=1.8; user-scalable=no;' name='viewport'/>
<h2>ESP8266 Led Matrix Display</h2>
<h3>Type something then press ENTER to display</h3>
<form>
  Message:<br>
  <input type="text" name="Message" size="40" value=""><br>
  <input type="submit" value="ENTER">
</form>
</html>
"""

import usocket as socket
import uselect as select

def client_handler(client_obj):
    get_message(client_obj)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 80))
server.listen(1)

message_list=[" "*tile + "Welcome "]
print(message_list)

def get_message(client_obj):
    request = client_obj.recv(1024)
    request = str(request)

    msg_list = request.split('/')
    parse_1=msg_list[1]
    parse_2=parse_1[9:len(parse_1)-5]
    parse_3=parse_2.split('+')
    parse_4=' '.join(parse_3)
    message = (" " * tile) + parse_4
    message_list.insert(0,message)
    message_list.pop()

    response = html
    
    client_obj.send(response)
    client_obj.close()

def display(s):
    for c in range(len(s)*8):
        device.fill(0)
        device.text(s,-c,0)
        device.show()
        time.sleep(0.05)

while True:
    r, w, err = select.select((server,), (), (), 1)
    if r:
        for readable in r:
            client, client_addr = server.accept()
            try:
                client_handler(client)
            except OSError as e:
                pass
            
    display(message_list[0])
