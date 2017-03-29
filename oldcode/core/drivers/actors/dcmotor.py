# -*- coding: utf-8 -*-

import RPi.GPIO as gpio

from ...config import config


class Motor(object):
    """
    Author: Marc Steinebrunner


    """
    pwmpin = None
    frequenz = None

    def __init__(self, frequenz):
        """
        Diese Funktion holt die Notwendingen Pinnummern von der Config
        """
        self.pwmpin = config.get_pins(self.__name__)
        self.frequenz = frequenz
        self.pwmpin = gpio.PWM(self.pwmpin, frequenz)
        self.pwmpin.start(0)

    def set_frequenz(self, frequenz):
        """
        Setzt die frequenz

        Args:       frequenz

        Returns:    -
        """
        self.frequenz = frequenz

    def rotate(self, speed):
        """
        Diese Funktion dient zum Drehen des Motors mit einer bestimmten
        Geschwindigkeit.

        Args:       speed   Die Geschwindigkeit mitder der Motor drehen soll
                            in Prozent

        Returns:    -
        """
        self.pwmpin.ChangeDutyCycle(speed)

    def __del__(self):
        """
        Durch diese Funktion kann man die motoren ausschalten dies ist für die Lande funktion wichtig
        Args:       -

        Returns:    -
        """
        self.pwmpin.stop()
        gpio.cleanup()
        gpio.output(self.pwmpin, LOW)
