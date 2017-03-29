# -*- coding: utf-8 -*-

from threading import Thread
import picamera as picam
import os
from ...config import config


class Picamera(object):
    """
    Author: Raphael Kreft
    Diese Klasse abstrahiert ein Raspberry-PI Kamera und ermöglicht deren Nutzung.
    """

    def __init__(self):
        """
        Diese Funktion wird beim erzeugen eine Objekts dieser Klasse ausgeführt.
        Sie erstellt ein neues Picamera-Objekt, mit dem in dieser Klasse dann
        gearbeitei wird.

        Args:       -

        Returns:    -
        """
        print("Camera-Objekt wird erzeugt...")
        self.__camera = picam.PiCamera()
        print("Setze Kameraauflösung...")
        self.__camera.resolution = (1280, 720)
        self.__thread = None

    @staticmethod
    def stream(ip, port):
        """
        Diese Dunktion beinhaltet den Stream-befehl

        Args:   port    Der Port auf dem der Stream gesendet wird
                ip      Die IP des Client an den der Stream geschickt werden soll.

        Returns:        -
        """
        os.system("raspivid -t 1 -o – | nc " + str(ip) + str(port))  # Bash-Kommando für den Stream über netcat

    def start_stream(self):
        """
        Diese Funktion startet den Stream mittels bash befehl.

        Args:       -

        Returns:    -
        """
        ip = Config.get_client_ip()  # hole ip von Config-Klasse
        port = Config.get_stream_port()  # hole port von Config-Klasse
        print("starte Stream...")
        self.__thread = Thread(target=self.stream, args=(ip, port))  # erzeuge globalen Thread
        self.__thread.start()  # starte den Thread

    def stop_stream(self):
        """
        Diese Funktion nutzt ein shell-kommando zum stoppen des videostreams.
        """
        self.__thread.join()  # beenden des Thread
