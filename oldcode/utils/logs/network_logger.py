# -*- coding: utf-8 -*-

import logging
import time
import os


class NetworkLogger(object):
    """
    Author: Raphael Kreft

    Instanzen dieser Klasse loggen die Kommunikation mit dem Client
    """

    def __init__(self):
        """
        Generate a new Folder to log in.
        """
        try:
            dir_name = str(time.time())
            os.mkdir(dir_name)
        finally:
            os.chdir(dir_name)

        logging.basicConfig(filename= "rootlogging-" + self.__name__ + ".log", level=logging.DEBUG)
        self.__logger = None
        self.new_logger()


    def new_logger(self):
        """
        Generate a new logger
        """
        self.__logger = logging.getLogger(self.__name__)
        self.__logger.setLevel(logging.INFO)
        filehandler = logging.FileHandler(str(time.day) + "-" + str(time.hour) + ".log")
        formatter = logging.Formatter('%(name)s - %(levelname)s : %(asctime)s - %(message)s')
        filehandler.setFormatter(formatter)
        self.__logger.addHandler(filehandler)

    def log(self,message, level='INFO'):
        """
        logs the message
        """
        message = str(message)
        if level == "CRITICAL":
            self.__logger.critical(message)
        elif level == "WARNING":
            self.__logger.warning(message)
        elif level == "INFO":
            self.__logger.info(message)
        elif level == "DEBUG":
            self.__logger.debug(message)
        else:
            self.__logger.debug("Could not log... unknown level")
