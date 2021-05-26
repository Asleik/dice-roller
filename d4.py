from dn import DN


class D4(DN):
    def __init__(self):
        super().__init__(4)

    def __str__(self):
        return str(f'd4: \n{self.__special_print()}')

    def __special_print(self):
        values = list(range(1, 5))
        a = str(self.value)
        values.remove(self.value)
        b = str(values.pop())
        c = str(values.pop())

        return '     /\\\n' \
               '    /a \\\n' \
               '   /    \\\n' \
               '  /      \\\n' \
               ' /        \\\n' \
               '/ b      c \\\n' \
               '------------\n'\
            .replace('a', a)\
            .replace('b', b)\
            .replace('c', c)
