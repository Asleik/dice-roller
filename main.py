from board import Board
from d4 import D4
from d6 import D6


def generaltest(number_of_dices):
    board = Board(number_of_dices)
    dices = board.dice_stack_creator()

    for dice in dices:
        dice.roll()
        print(f'{dice}: \n{dice.special_print()}')


def d4test():
    dice = D4()
    dice.roll()
    print(dice.special_print())


def d6test():
    dice = D6()
    dice.roll()
    print(dice.special_print())


generaltest(3)
