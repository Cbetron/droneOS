#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""motor.py:	Motor class"""

__author__ = "Raphael Kreft"
__copyright__ = "Copyright (c) 2016 Raphael Kreft"
__version__ = "Development v0.0"
__email__ = "raphaelkreft@gmx.de"
__status__ = "Dev"

import RPi.GPIO as gpio


class Motor(object):
    def __init__(self, pin, startspeed):
        self.pwmpin = gpio.PWM(pin)
        self.speed = startspeed

    def get_pin(self):
        return self.pwmpin

    def get_speed(self):
        return self.speed

    def change_frequenz(self, frequenz):
        self.pwmpin.ChangeFrequency(frequenz)

    def change_position(self, degrees):

