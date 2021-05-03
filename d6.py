from dice import Dice


class D6(Dice):
    def __init__(self):
        super().__init__(6)

    def __str__(self):
        return str(f'd6: {self.value}')

    def special_print(self):
        all_dots = list('abcdefghijl')
        dice_number = [1, 2, 3, 4, 5, 6]
        dice_dots = ['f', 'bj', 'afl', 'bhdj', 'agfel', 'acegil']
        map_of_dots = dict(zip(dice_number, dice_dots))

        dice_string = ' --------- \n' + \
                      '| a     g |\n' + \
                      '| b     h |\n' + \
                      '| c  f  i |\n' + \
                      '| d     j |\n' + \
                      '| e     l |\n' + \
                      ' --------- \n'

        # dots to paint
        for i in map_of_dots[self.value]:
            dice_string = dice_string.replace(i, 'o')
            all_dots.remove(i)

        for i in all_dots:
            dice_string = dice_string.replace(i, ' ')

        return dice_string


