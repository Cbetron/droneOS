import os


class Configuration(object):
    def __init__(self):
        self.configuration = {}
        if not os._exists("config.cfg"):
            raise FileNotFoundError

    def entry_exists(self, name):
        return True if name in self.configuration.keys() else False

    def get_value_by_name(self, name):
        if self.entry_exists(name):
            return self.configuration[name]
        else:
            raise NotImplemented

    def set_value(self, name, value):
        if not self.entry_exists(name):
            self.configuration += {name: value}

    def load_configuration(self):
        data = open("configuration.cfg").readlines()
        splitted = [line.split("=") for line in data]
        self.configuration = dict(splitted)

    def save_configuration(self):
        with open("configuration.cfg", "w") as cfg:
            for key, value in self.configuration.items():
                cfg.write(key + "=" + value + "\n")
            cfg.close()

