#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""controller.py:	Iniztialisation of sensors and actors. Controls the Hardware of the Drohnes"""

__author__ = "Raphael Kreft"
__copyright__ = "Copyright (c) 2016 Raphael Kreft"
__version__ = "Development v0.0"
__email__ = "raphaelkreft@gmx.de"
__status__ = "Dev"

import threading
import time

from control.drivers.sensors.interface import  Interface

class Controller(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.SensorInterface = Interface()
        self.sensorsrunning = {} # dictionary with the active sensors the user want to have data from
        self.running = None
        self.name = name

    def start(self):
        self.running = True
        self.run()

    def stop(self):
        print("Python Hardwarecontroller Controller {} shutdown!".format(self.name))
        self.running = False

    def run(self):
        while self.running:
            print("Iam running")

    def sensor_chain(self):