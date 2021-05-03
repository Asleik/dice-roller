from dice import Dice


class D4(Dice):
    def __init__(self):
        super().__init__(4)

    def __str__(self):
        return str(f'd4: {self.value}')

    def special_print(self):
        values = [1, 2, 3, 4]
        values.remove(self.value)
        return str(f'     /\\\n') + \
               str(f'    /{self.value} \\\n') + \
               str(f'   /    \\\n') + \
               str(f'  /      \\\n') + \
               str(f' /        \\\n') + \
               str(f'/ {values.pop()}      {values.pop()} \\\n') + \
               str(f'------------\n')
