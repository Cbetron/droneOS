# -*- encoding: utf-8 -*-

import threading
import time

from ..drivers import ultraschallsensor


class UsController(threading.Thread()):
    """
    Author: Raphael Kreft

    Diese Klasse ist ein Threadobjekt und verwaltet die ultraschallsensoren.
    """

    def __init__(self):
        """
        Erzeugt Instanzen für Ultraschallsensoren
        """
        threading.Thread.__init__(self)
        self.us_front = ultraschallsensor.Ultraschallsensor('front')
        self.us_left = ultraschallsensor.Ultraschallsensor('left')
        self.us_right = ultraschallsensor.Ultraschallsensor('right')
        self.us_bottom = ultraschallsensor.Ultraschallsensor('bottom')
        self.__dist_front = None
        self.__dist_left = None
        self.__dist_right = None
        self.__dist_bottom = None
        self.running = None

    def run(self):
        """
        Überschreibt die Distanzvariabeln
        """
        while self.running:
            self.__dist_front = self.us_front.distanz()
            self.__dist_left = self.us_left.distanz()
            self.__dist_right = self.us_right.distanz()
            self.__dist_bottom = self.us_bottom.distanz()
            time.sleep(0.01)

    def start(self):
        """
        Startet run-methode
        """
        self.running = True
        self.start()

    def stop(self):
        """
        Stopt den Thread
        """
        self.running = False

    def get_dist(self, device):
        """
        Get the distances
        :param device:
        :return:
        """
        if device == 'front' or device == 'us_front':
            return self.__dist_front
        elif device == 'left' or device == 'us_left':
            return self.__dist_left
        elif device == 'right' or device == 'us_right':
            return self.__dist_right
        elif device == 'bottom' or device == 'us_bottom':
            return self.__dist_bottom
        else:
            print(str(device) + "cannot found")
