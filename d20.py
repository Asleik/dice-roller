from dice import Dice


class D20(Dice):
    def __init__(self):
        super().__init__(20)

    def special_print(self):
        dice_number = [1, 2, 3, 4, 5, 6]
        dice_dots = [['f'], ['b', 'j'], ['a', 'f', 'l'], ['b', 'h', 'd', 'j'],
                     ['a', 'g', 'f', 'e', 'l'], ['a', 'c', 'e', 'g', 'h', 'l']]
        map = dict(zip(dice_number, dice_dots))
        print(map)
        return str(f' --------- ') + \
               str(f'| {a}     {g} |') + \
               str(f'| {b}     {h} |') + \
               str(f'| {c}  {f}  {i} |') + \
               str(f'| {d}     {j} |') + \
               str(f'| {e}     {l} |') + \
               str(f' --------- ')
