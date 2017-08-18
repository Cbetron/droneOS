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

from control.drivers.sensors.interface import  Interface as S_INTERFACE
from control.drivers.actors.interface import  Interface as A_INTERFACE
from control.sequences import basics

class DeviceHandler(object):
	def __init__(self):
		self.devices = dict()

	def load(self):
		with open("devices.dat", "r").readlines() as data:
			for d in data:
				if d.startswith(":"):
					key, driver, val, group = d.split("-")
					self.devices += {key: [driver,list(val.split(",")),group]}
				else:
					continue
	
	def write(self):
		pass			
class Controller(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.SensorInterface = S_INTERFACE()
        self.ActorInterface = A_INTERFACE()
        self.running = None
        self.name = name

    def start(self):
        self.running = True
        self.SensorInterface.start()
        self.ActorInterface.start()
        self.run()

    def stop(self):
        print("Python Hardwarecontroller Controller {} shutdown!".format(self.name))
        self.running = False

    def run(self):
        while self.running:
            pass
