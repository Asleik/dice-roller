from dn import DN


class D20(DN):
    def __init__(self):
        super().__init__(20)

    def __special_print(self):
        """Not in the mood for some ASCII ART, sry."""
        pass
