class ShippingContainer:

    next_serial = 1000

    @classmethod
    def _get_next_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    def __init__(self, owner_code, contents) -> None:
        self.owner_code=owner_code
        self.contents=contents
        self.serial = ShippingContainer._get_next_serial()
        