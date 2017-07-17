#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""control-connection.py:	Description of pythonfile.py"""

__author__ = "Raphael Kreft"
__copyright__ = "Copyright (c) 2016 Raphael Kreft"
__version__ = "Development v0.0"
__email__ = "raphaelkreft@gmx.de"
__status__ = "Dev"

# Systemimports
import pickle
import socket
import subprocess
import sys
import os
import threading


def accepted_ips():
	with open("acc_ip.dat", "r") as file:
		return file.readlines()


class SimplePacker(object):
    @staticmethod
    def pack_data(data, cypher=None):
        serialized = pickle.dumps(data)
        if not cypher:
            return serialized
        else:
            return cypher(serialized)

    @staticmethod
    def unpack_data(data, cypher=None):
        unserialized = pickle.loads(bytes(data))
        if not cypher:
            return unserialized
        else:
            return cypher(unserialized)


class SocketController(threading.Thread):
    def __init__(self, data_packer=SimplePacker, sock=None, port=TCP_PORT, max_clients=MAX_CLIENTS, buffersize=BUFFER_SIZE):
        super().__init__()
        if not sock:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.bind(("localhost", port))  # bind Socket to TCP-Port
        self.max_clients = max_clients
        self.packer = data_packer
        self.buffersize = buffersize
        self.connections = []
        self.running = False

    def start(self):
        self.running = True
        self.run()

    def run(self):
        while self.running:
            self.sock.listen(self.max_clients)
            connection, addr = self.sock.accept()
            print("SocketController: Got Connection from: {}".format(addr))
            if addr not in [connection.get_address() for connection in self.connections] and addr[0] in accepted_ips():
                Conn = ConnectionHandler(connection, addr, self.packer, self.buffersize)
                Conn.start()
                self.connections.append(Conn)

    def stop(self):
        for c in self.connections:
            c.stop()
            c.join()
        self.running = False
        self._stop()


class ConnectionHandler(threading.Thread):
    def __init__(self, c, addr, datapacker, buffersize):
        super().__init__()
        self.connection = c
        self.conn_addr = addr
        self.packer = datapacker
        self.buffersize = buffersize
        self.running = False

    def recieve(self):
        while True:
            print("Connectionhandler {}: recieving data...".format(self.conn_addr))
            data = self.connection.recv(self.buffersize)
            if not data:
                break
            else:
                return self.packer.unpack_data(data)

    def send(self, data):
        data = self.packer.pack_data(data)
        self.connection.sendall(data)

    def start(self):
        self.running = True
        self.run()

    def run(self):  # Insert your Handling of Clients Here
        while self.running:
            query = str(self.recieve())
            print("Connectionhandler {}: recieved Order: {}".format(self.conn_addr, query))
            if query == "S1":
                print("Connectionhandler {}: Analyse System...".format(self.conn_addr))
                self.send(SystemInfo().systeminfo())
            elif query == "S2":
                print("Connectionhandler {}: Shutdown Order recieved!".format(self.conn_addr))
                sys.exit(0)
            else:
                continue


class ControlConnection(threading.Thread):
	def __init__()