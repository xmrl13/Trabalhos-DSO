from sqlite3 import Date
from quarto import Quarto
from cliente import Cliente


class Reserva:
    def __init__(self, quarto: Quarto, cliente: Cliente, data: Date):
        self.__quarto = quarto
        self.__cliente = cliente
        self.__data = data
    
    @property
    def quarto(self):
        return self.__quarto

    @quarto.setter
    def quarto(self, quarto):
        self.__quarto = quarto

    @property
    def cliente(self):
        return self.__cliente
    
    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente
    
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data
