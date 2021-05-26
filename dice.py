from dn import DN
from d4 import D4
from d6 import D6
from d8 import D8
from d10 import D10
from d12 import D12
from d20 import D20


class Dice:
    """This class is a Factory"""
    @staticmethod
    def creator(dice_type):
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
        return DN(dice_type)
