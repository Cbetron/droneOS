# -*- coding: utf-8 -*-

"""
@author: Raphael Kreft

Dieses Modul dient zu ansteuern des Relais für die Servos zur Bewegung.
"""

import RPi.GPIO as GPIO
from ...config import config

try:
    Config = config.Config()
except:
    print("Onjekt existiert schon")


class MovementRelais(object):
    """
    Author: Raphael Kreft
    """

    def __init__(self):
        """
        Holt die Pinnummer, setzt den GPIO-Modus und schaltet den Pin aus.

        Args:       -

        Returns:    -
        """
        self.relais_pin = Config.getpin("relais")
        GPIO.setmode(GPIO.BCM)  # GPIO Nummern statt Board Nummern
        GPIO.setup(self.relais_pin, GPIO.OUT)  # GPIO Modus zuweisen
        GPIO.output(self.relais_pin, GPIO.LOW)  # aus

    def switch(self, state):
        """
        Schaltet das Relais an.

        Args:       state   On or Off

        Returns:    -
        """
        if state == "Off":
            GPIO.output(self.relais_pin, GPIO.LOW)  # aus
        elif state == "On":
            GPIO.output(self.relais_pin, GPIO.HIGH)  # an
        else:
            pass

    def __del__(self):
        """
        switch off for safety
        """
        self.switch('Off')
