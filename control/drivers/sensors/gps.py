# -*- coding: utf-8 -*-

import threading
import gps  # gpsd und gpsd-clients müssen installiert global sein


class GpsInterviewer(threading.Thread()):
    """
    Author: Raphael Kreft

    Diese Klasse läuft ab dem start als Thread(run-Funktion wird durchlaufen)
    Sie dient als Gps_Interviewer und ermöglicht das abrufen von Daten.
    """

    def __init__(self):
        """
        Diese Funktion wird bei der Erzeugung von einem Objekt dieser Klasse aufgerufen.
        Hier erfolgt das Setup für Die GPS-Ortung.

        Args:       -

        Returns:    -
        """
        threading.Thread.__init__(self)
        self.gpsd = gps(mode=WATCH_ENABLE)
        self.current_value = None
        self.running = None

    def run(self):
        self.running = True
        while self.running:
            self.gpsd.next()

    def stop(self):
        self.running = False
        self.join()
        self.gpsd.stop()

    def get_speed(self):
        """
        Diese Funktion liest die Geschwindigkeit und gibt Sie
        an die Aufrufende Stelle zurrück.

        Args:       -

        Returns:    speed   Die ausgelesene Geschwindigkeit
        """
        speed = self.gpsd.fix.speed
        return speed

    def get_longitude(self):
        """
        Diese Funktion liest den Längengrad und gibt ihn
        an die Aufrufende Stelle zurrück.

        Args:       -

        Returns:    longitude   Der Ausgelesene Längengrad
        """
        longitude = self.gpsd.fix.longitude
        return longitude

    def get_latitude(self):
        """
        Diese Funktion liest den Breitengrad und gibt ihn
        an die Aufrufende Stelle zurrück.

        Args:       -

        Returns:    longitude   Der Ausgelesene Breitengrad
        """
        latitude = self.gpsd.fix.latitude
        return latitude

    def get_position(self):
        """
        Diese Funktion liest die Position und gibt sie
        an die Aufrufende Stelle zurrück.

        Args:       -

        Returns:    position   Die Ausgelesne Position
        """
        position = self.gpsd.fix.track
        return position
