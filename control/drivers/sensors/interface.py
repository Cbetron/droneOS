#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""interface.py:	Interface which manages the sensors"""

__author__ = "Raphael Kreft"
__copyright__ = "Copyright (c) 2016 Raphael Kreft"
__version__ = "Development v0.0"
__email__ = "raphaelkreft@gmx.de"
__status__ = "Dev"

"""Every sensor has its own identifier: Ultraschall: u0, u1...
                                        Gps: g0"""

import time
import threading


class Data(object):
    __slots__ = ["data", "si", "id", "time"]
    def __init__(self, d, si, id):
        self.data = d
        self.si = si
        self.id = id
        self.time = time.time()


class Pool(object):
    def __init__(self, ids=None, dataamount=100):
        if ids is None:
            ids = []
        self.ids = ids
        self.dataamount = dataamount
        self.pool = {}

    def add_data(self, id, datapoint):
        self.pool[id].append(datapoint)

    def check_dataamount(self):
        for sensor in self.pool:
                while len(sensor) > self.dataamount:
                    del sensor[0]

    def get_data(self, id, amount=1):
        return self.pool[id][:amount]


class Interface(object):
    def __init__(self):
        self.sensors = []
        self.datapool = Pool()

    def get_sensor_data(self, sensorid, amount=1):
        return self.datapool.get_data(sensorid, amount)

    def add_sensor_dat(self, sensorid, data, si):
        self.datapool.add_data(sensorid, Data(data, si, sensorid))
        self.datapool.check_dataamount()