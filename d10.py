from dice import Dice


class D10(Dice):
    def __init__(self):
        super().__init__(10)


    def special_print(self):
        values = [1, 2, 3, 4]
        values.remove(super().value)
        return str(f'     /\\\n') + \
               str(f'    /{super().value} \\\n') + \
               str(f'   /    \\\n') + \
               str(f'  /      \\\n') + \
               str(f' /        \\\n') + \
               str(f'/ {values.pop()}      {values.pop()} \\\n') + \
               str(f'------------\n')
