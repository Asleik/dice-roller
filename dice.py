import random


class Dice:
    def __init__(self, sides):
        self._sides = sides
        self._value = 0

    def roll(self):
        self._value = random.randrange(1, int(self._sides)+1)

    @property
    def value(self):
        return self._value

    def __str__(self):
        return str(f'd{self._sides}: {self.value}')
