

class Mobilia:
    def __init__(self, descricao: str, quantidade: int):
        self.__descricao = descricao
        self.__quantidade = quantidade

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descrica(self, descricao: str):
        self.__descricao = descricao

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade: int):
        self.__quantidade = quantidade
    