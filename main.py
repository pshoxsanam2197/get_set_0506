class Odam:
    def __init__(self, ism):
        self.__ism = ism

    def get_ism(self):
        return self.__ism

    def set_ism(self, ism):
        self.__ism = ism

o = Odam("Ali")
print(o.get_ism())

o.set_ism("Vali")
print(o.get_ism())
