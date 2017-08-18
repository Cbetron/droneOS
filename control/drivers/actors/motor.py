!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://goo.gl/o1Uo6S  Datasheet & Erklärung
"""motor.py:	Motor class"""

__author__ = "Marc Steinebrunner oversight Raphael Kreft"
__copyright__ = "Copyright (c) 2017 Marc Steinebrunner"
__version__ = "Development v0.02"
__email__ = "marc.steinebrunner@gmail.com"
__status__ = "Dev"

""" 
Link to Data Sheet: https://goo.gl/o1Uo6S 
This class was written in dependence on the IPC L293D link to the data sheet above. 
Pin IN1 and Pin IN2 must be connected to the 2 IN ports on the same page.  
The EN must be connected to the EN pin on the same page as IN1 and IN2. 
Pins marked with 0V must be connectet with a Ground Port. 
The Pin V+(L293D Pin 16) is the Power for the Board (5V) 
The Pin +Vmotor (L293D Pin 8) is the Power for the Motor's (4.5V - 36V) 
""" 


import RPi.GPIO as gpio


class Motor(object):

    def __init__(self, EN, IN1, IN2):
        gpio.setmode(gpio.BOARD)
        gpio.setup(EN, gpio.OUT)
        
        
        self.pwmpin = gpio.PWM(EN, 100)
        self.pin1 = IN1
        self.pin2 = IN2
        self.percent = None

        gpio.setup(self.pin1, gpio.OUT)
        gpio.setup(self.pin2, gpio.OUT)

    def get_pwmpin(self):
        return self.pwmpin

    def get_pin1(self):
        return self.pin1

    def get_pin2(self):
        return self.pin2

    def get_speed(self):
        return self.percent

    def clockwise(self):
        gpio.output(self.pin1, True)
        gpio.output(self.pin2, False)

    def counter_clockwise(self):
        gpio.output(self.pin1, False)
        gpio.output(self.pin2, True)

    def change_frequenz(self, frequenz):
        self.pwmpin.ChangeFrequency(frequenz)

    def change_speed(self, percent):
        self.percent = percent
        self.pwmpin.ChangeDutyCycle(self.percent)

    def __del__(self):
        gpio.cleanup(EN,IN1,IN2)
