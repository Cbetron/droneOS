class HardwareConfiguration(object):
    def __init__(self):
        self.config = {}
        self.load_configuration()

    def load_configuration(self):
        data = open("hardware.cfg").readlines()
        for line in data:
            if line.startswith("#"):
                continue
            else:
                split = line.split(",")
                self.config += {{"sensorid": split[0] , {"sensortype": split[1], "infoslot": split[2]}} #sensortype is Objectname of Hardwaredriver

    def get_configuration(self):
        return self.config