#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""servo.py:	Servo class"""

__author__ = "Raphael Kreft"
__copyright__ = "Copyright (c) 2017 Raphael Kreft"
__version__ = "Development v0.0"
__email__ = "raphaelkreft@gmx.de"
__status__ = "Dev"

import RPi.GPIO as gpio


class Servo(object):
    def __init__(self, pin, frequenz):
        self.frequenz = frequenz
        self.pwmpin = gpio.PWM(pin, frequenz)

    def get_frequenz(self):
        return self.frequenz

    def get_pin(self):
        return self.pwmpin

    @staticmethod
    def degree_to_cycle(degrees):
        return 2.5 + degrees * (10 / 180)

    def change_frequenz(self, frequenz):
        self.pwmpin.ChangeFrequency(frequenz)

    def change_position(self, degrees):
        self.pwmpin.ChangeDutyCycle(self.degree_to_cycle(degrees))
