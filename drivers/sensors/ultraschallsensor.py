#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""ultraschallsensor.py:	Ultrashallsensor class"""

__author__ = "Raphael Kreft"
__copyright__ = ""
__version__ = "Development v0.01"
__email__ = "raphaelkreft@gmx.de"
__status__ = "Dev"


import time
import RPi.GPIO as gpio

from ...config import config


class Ultraschallsensor(object):

    #Diese Klasse abstrahiert einen Ultraschallsensor vom Typ: HC-SR04

    def __init__(self, identifier=__name__):
        self.ID = identifier
        pins = Config.getPins(self.ID)

        self.GPIO_Trigger = pins[0]
        self.GPIO_Echo = pins[1]

        gpio.setup(self.GPIO_Trigger,gpio.OUT)
        gpio.setup(self.GPIO_Echo,gpio.IN)

    def distanz(self):
        gpio.output(GPIO_Trigger, True)  # Der Trigger versendet ein Signal
        time.sleep(0.0001)
        gpio.output(GPIO_Trigger, False)

        startzeit = time.time()  # Startzeit und Stopzeit initialisieren
        stopzeit = time.time()

        while gpio.input(GPIO_Echo) == 0:  # Startzeit speichern
            startzeit = time.time()

        while gpio.input(GPIO_Echo) == 1:  # Stopzeit speichern
            stopzeit = time.time()

        return ((stopzeit - startzeit) * 34300) / 2
