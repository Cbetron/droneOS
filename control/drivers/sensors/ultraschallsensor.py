# -*- coding: utf-8 -*-

import time
import RPi.GPIO as gpio


class Ultraschallsensor(object):
    """
    Author: Raphael Kreft

    Diese Klasse abstrahiert einen Ultraschallsensor vom Typ: HC-SR04
    """

    def __init__(self, triggerpin, echopin, identifier=__name__):
        """
        Diese Funktion wird direkt nach der Erzeugung eines Objekts dieeser Klasse aufgerufen.
        Hierbei werden die Anschlusspins des Ultraschallsensors mit Hilfe der Funktion "setPins"
        gesetzt.

        Args:       -

        Returns:    -
        """
        self.ID = identifier
        self.si = "metre"
        self.GPIO_Trigger = triggerpin
        self.GPIO_Echo = echopin
        self.set_pins(self.GPIO_Trigger, self.GPIO_Echo)

    def get_id(self):
        return self.ID

    def set_pins(self, gpio_trigger, gpio_echo):
        """
        Mit Hilfe dieser Funktion können die Anschlusspins des Ultraschallsensors
        gesetzt werden.

        Args:       GPIO_Trigger    Der Anschlusspin des Sensors mit dem gesendet wird
                    GPIO_Echo       Der Pin an dem später die Eintreffenden Daten ausgelesen werden

        Returns:    -
        """
        self.GPIO_Trigger = gpio_trigger
        gpio.setup(gpio_trigger, gpio.OUT)
        self.GPIO_Echo = gpio_echo
        gpio.setup(gpio_echo, gpio.IN)

    def distanz(self):
        """
        Diese Funktion nutzt den Ultraschallsensor zur ermittlung der aktuellen
        Distanz von etwas.

        Args:       -

        Returns:    distanz     Die errechnete Distanz, die nun Zurrückgegeben wird
        """
        gpio.output(self.GPIO_Trigger, True)  # Der Trigger versendet ein Signal
        time.sleep(0.0001)
        gpio.output(self.GPIO_Trigger, False)

        startzeit = time.time()  # Startzeit und Stopzeit initialisieren
        stopzeit = time.time()

        while gpio.input(self.GPIO_Echo) == 0:  # Startzeit speichern
            startzeit = time.time()

        while gpio.input(self.GPIO_Echo) == 1:  # Stopzeit speichern
            stopzeit = time.time()

        zeitspanne = stopzeit - startzeit  # Distanz berechnen
        distanz = (zeitspanne * 34300) / 2

        return distanz

    def get_sensor_data(self):
        return self.get_id(), self.si, self.distanz()
