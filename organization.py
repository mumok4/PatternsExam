class Organization:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__initialized = False
        return cls.__instance

    def __init__(self, code=None, name=None, address=None, postal_code=None):
        if not self.__initialized:
            self.code = code
            self.name = name
            self.address = address
            self.postal_code = postal_code
            self.__initialized = True

    def update(self, code=None, name=None, address=None, postal_code=None):
        if code is not None:
            self.code = code
        if name is not None:
            self.name = name
        if address is not None:
            self.address = address
        if postal_code is not None:
            self.postal_code = postal_code
