# -*- coding: utf-8 -*-

from subprocess import call


class Picamera(object):
    """
    Author: Raphael Kreft
    Diese Klasse abstrahiert ein Raspberry-PI Kamera und ermöglicht deren Nutzung.
    """

    def __init__(self, fps, resolution):
        """
        Diese Funktion wird beim erzeugen eine Objekts dieser Klasse ausgeführt.
        Sie erstellt ein neues Picamera-Objekt, mit dem in dieser Klasse dann
        gearbeitei wird.

        Args:       fps: Frames per second camera

        Returns:    -
        """
        self.resolution = resolution
        self.fps = fps
        self.stream_status = False

    def make_stream(self, ip, port):
        """
        Diese Dunktion beinhaltet den Stream-befehl

        Args:   port    Der Port auf dem der Stream gesendet wird
                ip      Die IP des Client an den der Stream geschickt werden soll.

        Returns:        -
        """
        stream = "raspivid -o - -t 9999999 -w " + self.resolution[0] +" -h " + self.resolution[1] +" -fps " + self.fps +"|cvlc stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst="+ str(ip) +":" + str(port) +"'"
        return stream

    def start_stream(self, stream):
        """
        Diese Funktion startet den Stream mittels bash befehl.

        Args:       -

        Returns:    -
        """
        call([stream], shell=False)
        self.stream_status = True

    def stop_stream(self):
        """
        Diese Funktion nutzt ein shell-kommando zum stoppen des videostreams.
        """
        call(["pkill rpivid"], shell=False)
        call(["pkill vlc"], shell=False)
        self.stream_status = False

    def get_streamstatus(self):
        return self.stream_status
