

class Mobilia:
    def __init__(self, mobilia: str, quantidade: int):
        self.__mobilia = mobilia
        self.__quantidade = quantidade

    @property
    def mobilia(self):
        return self.__mobilia

    @mobilia.setter
    def mobilia(self, mobilia: str):
        self.__mobilia = mobilia

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade: int):
        self.__quantidade = quantidade
    