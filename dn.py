import random
from abc import abstractmethod


class DN:
    def __init__(self, sides):
        self.__sides = sides
        self.__value = random.randrange(1, int(self.__sides) + 1)

    @property
    def value(self):
        return self.__value

    @property
    def sides(self):
        return self.__sides

    def __str__(self):
        return str(f'd{self.__sides}: {self.__value}')

    @abstractmethod
    def __special_print(self):
        """Used for a graphical print"""
        pass

