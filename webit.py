
#WebIT written by Andi Dinata
#Under MIT License
#January 2018
#A simple module for a simple work to put any sensor reading to a webpage
#Add as many as reading as you want in the most simple way possible. Just web it.

import socket 
import websocket_helper

html = """<!DOCTYPE html>
<html>
<head> <title>ESP8266 Micropython Webserver</title> </head>
<h1>WebIT</h1>
<h2>Put any output to webpage</h2>
<form>
<font size="10" color="blue">  Your output reading is {0} </font></p>
<p>
<button style="font-size:30px;background-color:teal; height:70px;width:200px" name="BUTTON" value="btn" type="submit">REFRESH</button></p>
</form>
</html>
"""
data=0

class Webserver():
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(('', 80))
        self.s.listen(5)
            
    def output_feed(self):
	#below line is for the demo only, comment it and put your object here
        my_output=input("Type in any value and press ENTER to be printed in webpage: ")
        return my_output
    
    def start(self):
        while True:
            conn, addr = self.s.accept()
            request = conn.recv(1024)
            request = str(request)
            button = request.find('/?BUTTON=btn')
            
            if button == 6:
               data=self.output_feed()
	    else:
               data=0
            
            response = html
            
            conn.send(response.format(data))
            conn.close()
