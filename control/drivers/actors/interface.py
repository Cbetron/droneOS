#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""interface.py:	Interface which manages the actors"""

__author__ = "Raphael Kreft"
__copyright__ = "Copyright (c) 2016 Raphael Kreft"
__version__ = "Development v0.0"
__email__ = "raphaelkreft@gmx.de"
__status__ = "Dev"


class Interface(object):
    def __init__(self):
        self.actors = []

    def get_sensors(self):
        return self.actors

    def register_actor(self, sensor_obj):
        self.actors.append(sensor_obj)

    def unregister_actor(self, sensor_obj):
        self.actors.__delattr__(sensor_obj)

    def available(self, name):
        return True if name in [n.__name__ for n in self.actors] else False


