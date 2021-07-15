from Exceptions import WrongParametertypeError
import psutil
import time

class SystemHealth:

    __ram_percentage_max = None
    __ram_percentage_min = None

    def __init__(self):
        pass

    def setRAM_Percentage_max(self, value:float):
        if type(value) == type(1.0):
            self.__ram_percentage_max = value
        else: print("")




