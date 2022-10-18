from tipo_quarto import TipoQuarto

class Quarto:
	def __init__(self, numero_do_quarto: int, valor_diaria: float, tipo: TipoQuarto):
		self.__numero_do_quarto = numero_do_quarto
		self.__valor_diaria = valor_diaria
		self.__tipo = tipo
	
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
	def tipo(self):
		return self.__tipo
	
	@tipo.setter
	def tipo(self,tipo):
		self.__tipo = tipo

