# -*- coding: utf-8 -*-


import socket
import threading

from utils.logs import network_logger


class SteuerungsServer(object):
    """
    Author:	Raphael Kreft

    Diese Klasse dient als Steuerungsserver und arbeiet mit dem TCP-Protokoll
    Sie erbt von der Serverklasse.
    """
    Binding-Socket = None
    Comm-Socket = None
    logger = None

    def __init__(self):
        """
        Diese Funktion wird bei der Erzeugung eines Objektes dieser Klasse ausgeführt.
        sie führt die __init__-Funktion der Server-Klasse aus.

        Args:		-

        Returns:	-
        """
        self.logger = network_logger.NetworkLogger()
        print("get port from config...")
        self.port = Config.get_port("steuerung")
        self.host = socket.gethostbyname("HOSTNAME")
        print("setup the Binding-Socket...")
        self.Binding-Socket = socket.socket()  # Standart --> TCP-Server
        self.Binding-Socket.bind((self.host, self.port))

    @staticmethod
    def wait_for_connection():
        """
        Diese Funktion wartet auf eine Verbindung.

        Args:		-

        Returns:	c	Ein socket der von der accept()-funktion zurrückgegeben wird
        """
        self.logger.log('INFO',"Waiting for Client who connects")
        self.Binding-Socket.listen(1)
        connection, addr = self.Binding-Socket.accept()
        self.logger.log('INFO',"Connection from " + str(addr))
        return connection

    @staticmethod
    def sending(data):
        """
        Diese Funktion sendet Daten.

        Args:		data	die Daten, die gesendet werden sollen
                socket	der socket auf dem die Daten gesendet werden sollen.

        Returns:	-
        """
        self.logger.log('INFO',"Sending: " + str(data))
        data = data.encode('utf-8')
        self.Comm-Socket.send(data)
        self.logger.log('INFO',"Sended Data")

    @staticmethod
    def recieving():
        """
        Diese Funktion wartet auf ankommende Daten und gibt diese
        an die aufrufende Stelle zurrück.

        Args:		socket	Der socket vondem die Daten geholt werden sollen

        Returns:	data	die decodierten Daten
        """
        data = self.Comm-Socket.recv(1024).decode('utf-8')
        self.logger.log('INFO',"Recieved Data:  " + str(data))
        return data

    def run(self):
        """
        Diese Funktion nimmt Befehle entgegen und leitet diese
        zur steuerung des roboters weiter.

        Args:		-

        Returns:	-
        """
        self.Comm-Socket = self.wait_for_connection()
        try:
        while True:
            data = self.recieving()
            print(data)
        finally:
            self.Comm-Socket.close()

    def reset(self):
        """
        Diese Funktion wird zum reset der Verbindung ausgeführt.

        Args:		-

        Returns:	-
        """
        self.Binding-Socket.close()
        self.__init__()

    def __del__(self):
        """
        Delete this object with closing sockets
        """
        self.Binding-Socket.close()
