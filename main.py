#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""pythonfile.py:	Description of pythonfile.py"""

__author__ = "Raphael Kreft"
__copyright__ = "Copyright (c) 2016 Raphael Kreft"
__version__ = "Development v0.0"
__email__ = "raphaelkreft@gmx.de"
__status__ = "Dev"

#Systemimports
import sys
import threading

#Lokalimports
import connection.connectioncontroller as ccr
import control.controller as ccontrol
import config.config as cfg
import brain.manualcontrol as bmc

# version info for Updates
VERSION = "0.0"


# Exit codes
EXIT_OK = 0     # OK
EXIT_HELP = 1   # Help text printed
EXIT_ERR = 2    # Error

# Help-Text
HELP = "  DroneOS\n____________"


def die(cause, exit_code=EXIT_ERR):
    print(cause, file=sys.stderr)
    sys.exit(exit_code)


def print_info(version_only = False):
    print("Version: ", VERSION, file=sys.stderr)
    if not version_only:
        print(HELP, file=sys.stderr)
    sys.exit(EXIT_HELP)


class Drone(threading.Thread):
	def __init__(self, brain, control, connection, config):
		super().__init__()
		self.brain = brain
		self.control = control
		self.connection = connection 
		self.config = config

	def start(self):
		self.running = True
		self.run()

	def run(self):
		while self.running:
			query = self.connection.recieve()
			self.brain.compute(query)




if __name__ == "__main__":
	pass