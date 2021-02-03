""" EE 250L Lab 02: GrovePi Sensors

List team members here.

Insert Github repository link here.
"""

"""python3 interpreters in Ubuntu (and other linux distros) will look in a 
default set of directories for modules when a program tries to `import` one. 
Examples of some default directories are (but not limited to):
  /usr/lib/python3.5
  /usr/local/lib/python3.5/dist-packages

The `sys` module, however, is a builtin that is written in and compiled in C for
performance. Because of this, you will not find this in the default directories.
"""
import sys
import time
from grove_rgb_lcd import *
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')

import grovepi
from grove.adc import ADC

"""This if-statement checks if you are running this python file directly. That 
is, if you run `python3 grovepi_sensors.py` in terminal, this if-statement will 
be true"""
if __name__ == '__main__':
    PORT = 4    # D4

 #ARS to A0
potentiometer = 0
grovepi.pinMode(potentiometer,"INPUT")

#USR to D4
ultrasonic_ranger = 4

#variables to hold threshold and distance data
threshold = 0
dist = 0;

def thres_data()
  # Read sensor value from potentiometer
  sensor_value = grovepi.analogRead(potentiometer)
  return (sensor_value/10) #will go from 0.1 cm up to 51.2 cm

def dist_data()
  # Read distance value from Ultrasonic
  distance = grovepi.ultrasonicRead(ultrasonic_ranger)
  return distance

dist = dist_data()
threshold = threshold_data()

setRGB(0,255,0) #set color
textCommand(0x01) # clear display
textCommand(0x08 | 0x04) # display on, no cursor
textCommand(0x28) # 2 lines



if (dist <= threshold)
  setText_norefresh("OBJ PRES")
else 
  setText_norefresh("        ")
  
 
  
    while True:
        #So we do not poll the sensors too quickly which may introduce noise,
        #sleep for a reasonable time of 200ms between each iteration
        time.sleep(0.2)

        print(grovepi.ultrasonicRead(PORT))
