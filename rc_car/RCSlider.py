#RC Slider written by Andi Dinata
#Under MIT License
#January 2018
#An RC Car Webserver based on Webit.py
#HTML part is based on "https://stackoverflow.com/questions/48385068/esp8266-micropython-webserver-with-ajax"

import socket 
import websocket_helper
from rover import Motor
import time

m=Motor()

html = """<!DOCTYPE html>
<html>
<head> <title>RC Car </title> </head>
<meta content='width=device-width; initial-scale=1.8; maximum-scale=1.8; minimum-scale=1.8; user-scalable=no;' name='viewport'/>
<style>
    input[type=range]::-moz-range-thumb {
    width: 40px;
    height: 40px;
    background: black;
    }

    input[type=range] {
    -webkit-appearance: none;
    height: 5px;
    background: lightgrey;
    outline: none;
    position:absolute;
    }

    input[type=range]::-webkit-slider-thumb {
    -webkit-appearance: none;
    width: 40px;
    height: 40px;
    border-radius: 5px;
    background: black;
    }
</style>
</head>
  <body>       
    <input type='range' ontouchend='' onmouseup='' min='0' max='1000' value='500' id='sliderA' style='width:40%; -webkit-transform:rotate(270deg); left:60%; top:50%;'>
    <input type='range' ontouchend='resetB()' onmouseup='resetB()' min='0' max='1000' value='500' id='sliderB' style='width:40%; -webkit-transform:rotate(0deg); left:5%; top:50%;'>      
      <script>
      function myFunction(){
        var a = document.getElementById("sliderA").value;
        var b = document.getElementById("sliderB").value;        
        var xmlhttp=new XMLHttpRequest();
        xmlhttp.open("POST","Val=" + a + "B" + b + "C",true);
        xmlhttp.send();
      }
      setInterval(myFunction, 200);

      function resetB(){
        document.getElementById("sliderB").value = 500; 
      }
      </script>
  </body>
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
            ia = request.find("Val=")
            ib = request.find("B")
            ic = request.find("C")
            
            
            if ia > 0 :
              ValA = int(request[ia+4:ib])
              ValB = int(request[ib+1:ic])

              if ValA < 200:
                m.move(direction=0)
              else:
                m.move(ValA)
                
              if ValB > 700:
                m.stop(3)
                time.sleep(0.1)
                m.turn("right",0.3)
              elif ValB < 300:
                m.stop(3)
                time.sleep(0.1)
                m.turn("left",0.3)
            
            else:
              conn.sendall(html)
            
            conn.sendall('\n')
            conn.close()