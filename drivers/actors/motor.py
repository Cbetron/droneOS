#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""motor.py:	Motor class"""

__author__ = "Marc Steinebrunner"
__copyright__ = "Copyright (c) 2017 Marc Steinebrunner"
__version__ = "Development v0.02"
__email__ = "marc.steinebrunner@gmail.com"
__status__ = "Dev"

import RPi.GPIO as gpio

"""
Link to Data Sheet: https://goo.gl/o1Uo6S


This class was written in dependence on the IPC L293D link to the data sheet above.
Pin A and Pin B must be connected to the 2 IN ports on the same page. 
The PWMPin must be connected to the EN pin on the same page as A and B.
(For example, A = IN1, B = In2, PWMPin = EN1)

Pins marked with 0V must be connectet with a Ground Port.

The Pin V+(L293D Pin 16) is the Power for the Board (5V)
The Pin +Vmotor (L293D Pin 8) is the Power for the Motor's (4.5V - 36V)
"""


class Motor(object):
    def __init__(self, pin, startpercent, pin1, pin2):
        gpio.setup(self.pwmpin, gpio.OUT)
        self.pwmpin = gpio.PWM(pin, 500)
        self.pinA = pin1
        self.pinB = pin2
        self.percent = startpercent-1

        gpio.setup(self.pinA, gpio.OUT)
        gpio.setup(self.pinB, gpio.OUT)

        self.pwmpin.ChangeDutyCycle(self.percent)

    def get_pwmpin(self):
        return self.pwmpin

    def get_pinA(self):
        return self.pinA

    def get_pinB(self):
        return self.pinB

    def get_speed(self):
        return self.percent

    @staticmethod

    def clockwise(self):
        gpio.output(self.pinA , True)
        gpio.output(self.pinB , False)

    def counter_clockwise(self):
        gpio.output(self.pinA , False)
        gpio.output(self.pinB , True)

    def change_position(self, percent):
        self.pwmpin.ChangeDutyCycle(percent)
