#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sqlite3
import contextlib


class Config(object):
    """
    Author: Raphael Kreft

    Diese Klasse verwaltet alle zentralen, veränderbaren Werte im gesamten Programm, wie
    z.B Nutzerdaten, Pinbelegung usw...
    Models und Controller Können Daten lesen, Viewer können Werte ändern.
    Die Werte werden in Datein geschrieben, die dieser Klasse verwaltet.
    """

    def __init__(self):
        """
        Diese Funktion wird direkt nach der Erzeugung eines Objekts der Klasse
        "config" aufgerufen.

        Args:       -

        Returns:    -
        """
        pass

    def read_config(self):
        """
        Liest die Einträge der Configdate in ein Dictionary ein
        :return:
        """
        with contextlib.closing(open("config.txt", "r").readlines()) as cfg:
            config_dict = {}
            for line in cfg:
                if line.startswith("#"):
                    pass
                else:
                    cfg_object = line.split("=")
                    cfg_dict = {cfg_object[0], cfg_object[1]}
                    config_dict.update(cfg_dict)