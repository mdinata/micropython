# A Remote Control Car
This folder contains the wrapper for interacting 2 DC Motor connected to ESP8266 NodeMCU with Motor Shield and a webserver (based on webit.py) for controlling front end.<br >
![alt tag](http://andidinata.com/wp-content/uploads/2018/01/IMG20180127080608.jpg "ESP8266 NodeMCU on MotorShield")

## Usage
Copy rover.py and RCSlider.py to your ESP8266 and connect to it's access point e.g MicroPython-XXXX <br >
Then start the webserver. To make it start directly, copy main.py to your ESP8266 <br >
```
from RCSlider import Webserver
w=Webserver()
w.start()
```
Enjoy! <br >
![alt tag](http://andidinata.com/wp-content/uploads/2018/01/Screenshot_2018-01-27-08-07-02-19-1.png "Controlling front-end")
