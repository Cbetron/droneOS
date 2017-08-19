#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""controller.py:	Iniztialisation of sensors and actors. Controls the Hardware of the Drohnes"""

__author__ = "Raphael Kreft"
__copyright__ = "Copyright (c) 2016 Raphael Kreft"
__version__ = "Development v0.0"
__email__ = "raphaelkreft@gmx.de"
__status__ = "Dev"


from control.drivers.sensors.interface import Interface as S_INTERFACE
from control.drivers.actors.interface import Interface as A_INTERFACE
from control.sequences import basics


class DeviceHandler(object):
    def __init__(self):
        self.devices = dict()
        self.infotext = "# Devices file: All Devices(Motors, Sensors usw) are listed in this file.\n# The Controller " \
                        "is Using the Devices.dat for Controlling the drone\n" \ 
                        "# Devices are saved in this pattern: :Name-PathtoDriver-InitialvaluesforDriver-Group"
        self.actors = None
        self.sensors = None

    def split_groups(self):
        self.actors = dict([device for device in self.devices.values() if device[1][4] == "ACTOR"])
        self.sensors = dict([device for device in self.devices.values() if device[1][4] == "SENSOR"])

    def serialize(self):
        return [[key, *vals] for key, vals in self.devices.values()]

    def load(self):
        del self.devices
        with open("devices.dat", "r").readlines() as data:
            for d in data:
                if d.startswith(":"):
                    key, driver, val, group = d.split("-")
                    self.devices += {key: [driver, list(val.split(",")), group]}
                else:
                    continue
        self.split_groups()

    def write(self, devicedict):
        if self.devices is None:
            self.load()
        self.devices += devicedict
        self.split_groups()
        with open("devices.dat", "w") as file:
            file.write(self.infotext)
            for d in self.serialize():
                file.write(":{}-{}-{}-{}\n".format(*d))


class Controller(object):
    """Kontrolle der devices und bzw der Kompletten physischen Drohne"""
    def __init__(self, name):
        self.SensorInterface = S_INTERFACE()
        self.ActorInterface = A_INTERFACE()
        self.DeviceHandler = DeviceHandler()
        self.name = name

    def start(self):
        self.SensorInterface.start()
        self.ActorInterface.start()

    def stop(self):
        print("Python Hardwarecontroller Controller {} shutdown!".format(self.name))
        self.SensorInterface.stop()
        self.ActorInterface.stop()
        self.ActorInterface.join()
        self.SensorInterface.join()
