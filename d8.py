from dn import DN


class D8(DN):
    def __init__(self):
        super().__init__(8)

    def __str__(self):
        return str(f'd8: \n{self.__special_print()}')

    def __special_print(self):
        up_value = list(range(1, 9))
        down_value = [5, 6, 7, 8, 1, 2, 3, 4]
        map_of_dots = dict(zip(up_value, down_value))

        dice_string = '  /\\\n' \
                      ' /  \\\n' \
                      '/  a \\\n' \
                      '------\n' \
                      '\\ b  /\n' \
                      ' \\  /\n' \
                      '  \\/\n'

        dice_string = dice_string.replace('a', str(self.value)) \
                                 .replace('b', str(map_of_dots[self.value]))

        return dice_string
