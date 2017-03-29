# -*- coding: utf-8 -*-

from api.drivers.Adafruit_PWM_Servo_Driver import PWM
from ...config import config


class Servo(object):
    """
    Author: Raphael Kreft

    Diese Klasse abstrahiert einen Analog-Servo vom Typ
    """

    def __init__(self, identifier):
        """
        Diese Funktion wird direkt nach der Erzeugung des Objekts aufgerufen.
        Sie dient in diesem fall dazu, die Pins aus der Config-Klasse zu holen
        um korrekt angesteuert werden zu können.

        Args:		-

        Returns:	-
        """
        # initialisiere pwm --> neues Objekt der Klasse PWM aus dem Adafruitcode(Treiber für Servocontroller)
        self.__pwm = PWM()
        self.__pwm.setPWMFreq(60)
        self.__ID = identifier
        #Define the channel and set it up
        self.__channel = None
        self.set_channel()
        #Make config-Object

    def get_identifier(self):
        """
        Return the ID

        Args:       -
        Returns:    self.__ID   Die ID
        """
        return self.__ID

    def set_channel(self):
        """
        Diese Funktion dient zum setzen des channels, diesen holt sich die methode
        aus der config-Klasse.
        """
        # holen des Chanells von der Config-Klasses
        channel = Config.get_channel(self.__ID)
        self.__channel = channel
        print("set channel for Servo with Id: " + self.get_identifier())

    def get_channel(self):
        """
        Diese Funktion dient zum holen des PWM-Channels für den Servo-Selbst.
        Die Config-Klasse benutzt den Namen des Objekts um den Channel zu ermitteln.

        Args:		-

        Returns:	channel		Der channel, der von der config-Klasse geholt wird.
        """
        return self.__channel

    def set_servopulse(self, pulse=1.5):
        pulselength = 1000000  # 1,000,000 us per second
        pulselength /= 60  # 60 Hz
        print("%d us per period" % pulselength)
        pulselength /= 4096  # 12 bits of resolution
        print("%d us per bit" % pulselength)
        pulse *= 1000
        pulse /= pulselength
        self.__pwm.setPWM(self.__channel, 0, pulse)

    def __repr__(self):
        """
        Diese Funktion gibt beim Aufruf informationen über ein Objekt dieser Klasse an die
        Aufrufstelle zurrück.

        Args:	-

        Returns:	Der Return gibt die Nummern der Pins an die der Motor Angeschlossen ist an die Aufrufstelle Zurrück
        """
        return self.__channel, self.get_identifier()

    def __str__(self):
        """
        Diese Funktion wird aufgerufen wenn ein objekt von der methode "print()" aufgerufen wird.
        pwm-channer und ID werden zurrückgegeben.

        Args:		-

        Returns:	Die Verschiedenen Pin-Nummern
        """
        return "PWM_Channel: " + self.__channel + "\nID: " + self.get_identifier()

    def reset(self):
        """
        Diese Funktion wird aufgerufen um die Pins zurrückzusetzen und
        Anschliessend neu zuzuweisen. Dazu wid die __init__ funktion erneut aufgerufen.

        Args:		-

        Returns:	-
        """
        del self.__pwm
        self.__init__(self.get_identifier())
