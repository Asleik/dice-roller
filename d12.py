from dn import DN


class D12(DN):
    def __init__(self):
        super().__init__(12)

    def __special_print(self):
        """Not in the mood for some ASCII ART, sry."""
        pass
