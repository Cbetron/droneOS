# -*- coding: utf-8 -*-

from ..api.drivers import picam


def start_stream():
    """
    Diese Funktion startet den Stream.

    Args:           -

    Returns:        -
    """
    Picamera.start_stream()


def stop_stream():
    """
    Diese Funktion nutzt ein shell-kommando zum stoppen des videostreams.
    """
    Picamera.stop_stream()
