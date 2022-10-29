from model.quarto import Quarto


class Andar:
    def __init__(self, numero: int, quartos: list):
        self.__numero = numero
        self.__quartos = quartos

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def quartos(self):
        return self.__quartos

    # ficara no controlador de quartos tb
    def get_quarto_by_numero(self, numero: int):
        for quarto in self.__quartos:
            if quarto.numero_do_quarto == numero:
                return quarto

    # deve estar no controlador tb e se remover e add em um, deve ter no outro
    def remove_quarto(self, quarto: Quarto):
        for quarto_1 in self.__quartos:
            if quarto_1 == quarto:
                # Renomeei o indice do pop, estava: .pop(quarto), renomeei para .pop(quarto_1)
                self.__quartos.remove(quarto_1)
