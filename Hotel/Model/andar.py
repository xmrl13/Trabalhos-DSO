from model.quarto import Quarto

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
	
	@property
	def quartos(self):
		return self.__quartos

	def get_quarto_by_numero(self, numero: int): # ficara no controlador de quartos tb
		for quarto in self.__quartos:
			if quarto.numero_do_quarto == numero:
				return quarto

	def add_quarto(self,quarto: Quarto): 
		self.__quartos.append(quarto)
	
	def remove_quarto(self, quarto: Quarto ):   # deve estar no controlador tb e se remover e add em um, deve ter no outro
		for quarto_1 in self.__quartos:
			if quarto_1 == quarto:
				self.__quartos.pop(quarto)

