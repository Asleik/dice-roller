import re

from d10 import D10
from d12 import D12
from d20 import D20
from d4 import D4
from d6 import D6
from d8 import D8
from dice import Dice


class Board:
    def __init__(self, max_dices):
        self._max_dices = max_dices
        self._current_dices = 0
        print('Welcome do Dice Simulator')
        print(f'You have {self._max_dices} available')

    def __remaining_dices(self):
        return self._max_dices - self._current_dices

    def __update_dices_count(self, dice_quant):
        self._current_dices += dice_quant

    def __set_number_of_dices(self):
        # using RegEx to validade numbers
        pattern = re.compile(f'[0-{self.__remaining_dices()}]')
        while True:
            dices = input(f'How many dices you want to roll? (MAX: {self.__remaining_dices()})\n')
            match = pattern.fullmatch(dices)

            if not match:
                print('Not a valid number of dices imput')
            else:
                break
        return int(dices)

    def __dice_creator(self, dice_type):
        if dice_type == 4:
            return D4()
        if dice_type == 6:
            return D6()
        if dice_type == 8:
            return D8()
        if dice_type == 10:
            return D10()
        if dice_type == 12:
            return D12()
        if dice_type == 20:
            return D20()
        return Dice(dice_type)

    def dice_stack_creator(self):
        dices = []
        while self.__remaining_dices() > 0:
            dice_type = int(self.__set_dice_type())
            dice_quant = int(self.__set_number_of_dices())
            for index in range(dice_quant):
                dice = self.__dice_creator(dice_type)
                dices.append(dice)
            self.__update_dices_count(dice_quant)
        return dices

    def __set_dice_type(self):
        while True:
            size = input(f'Choose a dice size:\n d[4] d[6] d[8] d[10] d[12] d[20]\n')
            if size == 4 or 6 or 8 or 10 or 12 or 20:
                break
            else:
                print('Not a valid input')
        return size
