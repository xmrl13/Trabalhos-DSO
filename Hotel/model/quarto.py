

from model.mobilia import Mobilia


class Quarto:
	def __init__(self, numero_do_quarto: int, valor_diaria: float):
		self.__numero_do_quarto = numero_do_quarto
		self.__valor_diaria = valor_diaria
		self.__mobilias = []

	
	@property
	def numero_do_quarto(self):
		return self.__numero_do_quarto
	
	@numero_do_quarto.setter
	def numero_do_quarto(self,numero_do_quarto):
		self.__numero_do_quarto = numero_do_quarto
	
	@property
	def valor_diaria(self):
		return self.__valor_diaria
	
	@valor_diaria.setter
	def valor_diaria(self,valor_diaria):
		self.__valor_diaria = valor_diaria

	@property
	def mobilias(self):
		return self.__mobilias
	@mobilias.setter
	def mobilias(self, mobilias):
		self.__mobilias = mobilias
	
	def add_mobilia(self, descricao: str, quantidade: int):
		mobilia = Mobilia(descricao, quantidade)
		self.__mobilias.append(mobilia)
	
	def get_mobilias(self):
		return self.__mobilias