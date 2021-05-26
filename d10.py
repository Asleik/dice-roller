from dn import DN


class D10(DN):
    def __init__(self):
        super().__init__(10)

    def __special_print(self):
        """Not in the mood for some ASCII ART, sry."""
        pass
