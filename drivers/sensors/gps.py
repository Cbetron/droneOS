#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""servo.py:	Servo class"""

__author__ = "Raphael Kreft"
__copyright__ = ""
__version__ = "Development v0.01"
__email__ = "raphaelkreft@gmx.de"
__status__ = "Dev"

import threading
import gps  # gpsd und gpsd-clients müssen installiert global sein

gpsd = None


class GpsInterviewer(threading.Thread()):
    """
    Diese Klasse läuft ab dem start als Thread(run-Funktion wird durchlaufen)
    Sie dient als Gps_Interviewer und ermöglicht das abrufen von Daten.
    """

    def __init__(self):

        threading.Thread.__init__(self)
        global gpsd
        gpsd = gps(mode=WATCH_ENABLE)
        self.current_value = None
        self.running = None

        gpsp = Gps_interviewer()
        gpsp.start()

    def run(self):
        self.running = True
        global gpsd
        while self.running:
            gpsd.next()

    def stop(self):
        self.running = False
        self.join()

    def stop_gpsp(self):
        #Diese Funktion stopt den Gps_Interviewer.
        gpsp.stop()

    def get_speed(self):
        return gpsd.fix.speed

    def get_longitude(self):
        return gpsd.fix.longitude

    def get_latitude(self):
        return gpsd.fix.latitude

    def get_position(self):
        return gpsd.fix.track
