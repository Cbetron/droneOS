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

# Standart Network Constants
TCP_PORT = 5000
BUFFER_SIZE = 1024
MAX_CLIENTS = 1


def accepted_ips():
	with open("acc_ip.dat", "r") as file:
		return file.readlines()

def threadNames():
	return [t.getName() for t in threading.enumerate()]

def getThread_byName(name):
	tnb = zip(threading.enumerate(), threadNames())
	for t, n in tnb:
		if n is name:
			return t

class Queue(object):
	def __init__(self, max_size = 10):
		self.max_size = max_size
		self.datafield = []
	def qsize(self):
		return len(self.datafield)
	def empty(self):
		return True if self.qsize() is 0 else False
	def full(self):
		return True if self.qsize() >= max_size else False 
	def put(self, item):
		if not self.full():
			self.datafield.append(item)
		elif self.full():
			del self.datafield[0]
			self.datafield.append(item)
	def get(self):
		if not self.empty():
			data = self.datafield[0]
			del self.datafield[0]
			return data

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
            if addr not in [connection.get_address() for connection in self.connections] and addr[0] in accepted_ips(): # check if ip is permitted
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
            getThread_byName("controlconn").queue.put(query)
           	


class ControlConnection(threading.Thread):
	def __init__(self):
		self.Lock = threading.Lock
		self.running = False
		self.queue = Queue()
		self.SocketController = None
		self._port = TCP_PORT
		self._buffersize = BUFFER_SIZE
		self._max_clients = MAX_CLIENTS

	def get_port(self):
		return self._port

	def set_port(self, port, restart=False):
		self._port = port
		if restart:
			self.restartSocketControl()
	def get_buffersize(self):
		return self._buffersize

	def set_buffersize(self, buffersize, restart=False):
		self._buffersize = buffersize
		if restart:
			self.restartSocketControl()

	def get_maxc(self):
		return self.max_clients

	def set_maxc(self, maxc, restart=False):
		self._max_clients = maxc
		if restart:
			self.restartSocketControl()

	def restartSocketControl(self):
		self.Lock.accquire()
		del self.SocketController
		self.SocketController = SocketController(port=self.get_port(), buffersize=self.get_buffersize(), max_clients=self.get_maxc())
		self.Lock.release()

	def start(self):
		if "controlconn" not in threadNames():
			self.running = True
			self.SocketController = SocketController(port=self.get_port(), buffersize=self.get_buffersize(), max_clients=self.get_maxc())
			self.run()

	def get_query(self):
		return self.queue.get()

	def run(self):
		if not self.SocketController.isalive():
			self.SocketController.start()

	def stop(self):
		self.SocketController.stop()
		del self.queue