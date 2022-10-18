from quarto import Quarto

class Andar:
	def __init__(self, numero: int):
		self.__numero = numero
		self.__quartos = []
	
	@property
	def numero(self):
		return self.__numero
	
	@numero.setter
	def numero(self,numero):
		self.__numero = numero
	
	def add_quarto(self,quarto: Quarto):
		self.__quartos.append(quarto)
