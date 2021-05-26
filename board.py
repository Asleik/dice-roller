import re

from dice import Dice


class Board:
    def __init__(self):
        self.__dices = []  # DN storage list
        print('Welcome do DN Simulator.\n'
              'Creating a new Board.\n'
              '--------------------------------')
        self.__max_dices = self.__how_many_dices()
        self.__dice_stack_creator()  # Create dices
        self.dice_stack_printer()  # Print created dices

    def __how_many_dices(self, min_number=1, max_number=9) -> int:
        """This method will use RegEx to ensure the input will be a number
        between min_number and max_number"""
        dice_quantity = int
        match = None
        pattern = re.compile(f'[{min_number}-{max_number}]')

        while match is None:
            dice_quantity = input('How many dices do you want? '
                                  f'[Min:{min_number} - '
                                  f'Max: {max_number}]') \
                .replace(' ', '')
            match = re.fullmatch(pattern, dice_quantity)

        return int(dice_quantity)

    def print_available_dices(self):
        """Print how many dices are available for creation"""
        if self.__remaining_dices() == 1:
            print(f'You have {self.__remaining_dices()} dice available')
        else:
            print(f'You have {self.__remaining_dices()} dices available')

    def __remaining_dices(self) -> int:
        """Return the number of available dices for creation"""
        return self.__max_dices - len(self.__dices)

    def __dice_stack_creator(self):
        """Create the Dices"""
        print('--------------------------------\n'
              'Creating Dices.\n'
              '1) Choose how many dices will be created;\n'
              '2) Choose how many sides those above will have.\n'
              '3) Repeat until there is no more dices left.\n'
              '--------------------------------')
        while self.__remaining_dices() > 0:
            self.print_available_dices()

            dice_quantity = int(self.__how_many_dices
                                (1, self.__remaining_dices()))
            dice_sides = int(self.__how_many_dice_sides())

            for index in range(dice_quantity):
                dice = Dice.creator(dice_sides)
                self.__dices.append(dice)

    def dice_stack_printer(self):
        """Print the Dices"""
        print('--------------------------------\n'
              'Printing Dices.\n'
              '--------------------------------')

        for dice in self.__dices:
            print(dice)

    def __how_many_dice_sides(self):
        """Using RegEx to ensure it will be a number between 3 and 20, as
        4 is the minimum number of planes for the same sided Pyramid
        20 is just an arbitrary maximum number"""

        pattern = re.compile('([4-9])|(1[0-9])|20')
        match = None
        while match is None:
            sides = input('How many sides your dice will have? '
                          '[Min:4 - Max: 20]').replace(' ', '')
            match = re.fullmatch(pattern, sides)

        return sides
