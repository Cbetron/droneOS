#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://goo.gl/o1Uo6S  Datasheet & Erklärung
"""motor.py:	Motor class"""

__author__ = "Marc Steinebrunner oversight Raphael Kreft"
__copyright__ = "Copyright (c) 2017 Marc Steinebrunner"
__version__ = "Development v0.02"
__email__ = "marc.steinebrunner@gmail.com"
__status__ = "Dev"

import RPi.GPIO as gpio


class Motor(object):

    def __init__(self, pin, pin1, pin2):
        gpio.setmode(gpio.BOARD)
        gpio.setup(self.pwmpin, gpio.OUT)
        
        
        self.pwmpin = gpio.PWM(pin, 100)
        self.pin1 = pin1
        self.pin2 = pin2
        self.percent = None

        gpio.setup(self.pin1, gpio.OUT)
        gpio.setup(self.pin2, gpio.OUT)

        self.pwmpin.ChangeDutyCycle(initialspeed)

    def get_pwmpin(self):
        return self.pwmpin

    def get_pin1(self):
        return self.pin1

    def get_pin2(self):
        return self.pin2

    def get_speed(self):
        return self.speed

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
        self.change_speed(0)
