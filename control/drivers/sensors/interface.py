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


class Interface(threading.Thread):
    def __init__(self, delay=0.1):
        super().__init__()
        self.lock = threading.Lock()
        self.running = False
        self.sensors = []
        self.datapool = Pool()
        self._delay = delay

    def get_delay(self):
        return self._delay

    def set_delay(self, delay):
        self.lock.acquire()
        self._delay = delay
        self.lock.release()

    def get_sensors(self):
        return self.sensors

    def register_sensor(self, sensor_obj):
        self.lock.acquire()
        self.sensors.append(sensor_obj)
        self.lock.release()

    def unregister_sensor(self, sensor_obj):
        self.lock.acquire()
        self.sensors.__delattr__(sensor_obj)
        self.lock.release()

    def get_sensor_data(self, sensorid, amount=1):
        return self.datapool.get_data(sensorid, amount)

    def add_sensor_dat(self, sensorid, data, si):
        self.datapool.add_data(sensorid, Data(data, si, sensorid))
        self.datapool.check_dataamount()

    def start(self):
        self.running = True
        self.run()

    def run(self):
        while self.running:
            time.sleep(self.get_delay())
            for sensor in self.sensors:
                self.add_sensor_dat(*sensor.get_sensor_data())

    def stop(self):
        self.running = False
        del self.datapool
