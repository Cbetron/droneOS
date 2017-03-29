# -*- coding: utf-8 -*-

import threading
import gps  # gpsd und gpsd-clients müssen installiert global sein

gpsd = None


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
        global gpsd
        gpsd = gps(mode=WATCH_ENABLE)
        self.current_value = None
        self.running = None

    def run(self):
        self.running = True
        global gpsd
        while self.running:
            gpsd.next()

    def stop(self):
        self.running = False
        self.join()

    def start(self):
        """
        Diese Funktion startet den Gps_Interviewer.

        Args:       -

        Returns:    -
        """
        gpsp = Gps_interviewer()
        gpsp.start()

    def stop(self):
        """
        Diese Funktion stopt den Gps_Interviewer.
        """
        gpsp.stop()

    def get_speed(self):
        """
        Diese Funktion liest die Geschwindigkeit und gibt Sie
        an die Aufrufende Stelle zurrück.

        Args:       -

        Returns:    speed   Die ausgelesene Geschwindigkeit
        """
        speed = gpsd.fix.speed
        return speed

    def get_longitude(self):
        """
        Diese Funktion liest den Längengrad und gibt ihn
        an die Aufrufende Stelle zurrück.

        Args:       -

        Returns:    longitude   Der Ausgelesene Längengrad
        """
        longitude = gpsd.fix.longitude
        return longitude

    def get_latitude(self):
        """
        Diese Funktion liest den Breitengrad und gibt ihn
        an die Aufrufende Stelle zurrück.

        Args:       -

        Returns:    longitude   Der Ausgelesene Breitengrad
        """
        latitude = gpsd.fix.latitude
        return latitude

    def get_position(self):
        """
        Diese Funktion liest die Position und gibt sie
        an die Aufrufende Stelle zurrück.

        Args:       -

        Returns:    position   Die Ausgelesne Position
        """
        position = gpsd.fix.track
        return position
