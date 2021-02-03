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
from RPLCD import CharLCD
lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[40, 38, 36, 32, 33, 31, 29, 23])
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

helper1 = 0
helper2 = 0
threshold = 0
dist = 0;
lcd.clear()

class threshold_data(ADC):
    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC()
 
    @property
    def value(self):
        return self.adc.read(self.channel)


def dist_data()
  # Read distance value from Ultrasonic
  distant = ultrasonicRead(ultrasonic_ranger)
  return distant

    while True:
        #So we do not poll the sensors too quickly which may introduce noise,
        #sleep for a reasonable time of 200ms between each iteration
        dist = dist_data()
        threshold = threshold_data(ADC)
        lcd.cursor_pos = (0,0)
        lcd.write_string(dist_data())
        lcd.cursor_pos = (1,0)
        lcd.write_string(threshold_data())
        if (dist == threshold):
            lcd.cursor_pos = (0, 6)
            lcd.write_string(u'OBJ PRES')
        else if (dist > threshold):
            lcd.cursor_pos = (0, 6)
            lcd.write_string(u'        ')
           
          time.sleep(0.2)

        print(grovepi.ultrasonicRead(PORT))
