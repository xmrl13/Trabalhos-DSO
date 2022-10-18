
class TipoQuarto:

	def __init__(self,tamanho_quarto: float, quantidade_camas: int, jacuzzi: bool):
		self.__tamanho_quarto = tamanho_quarto
		self.__quantidade_camas = quantidade_camas
		self.__jacuzzi = jacuzzi
	
	@property
	def tamanho_quarto(self):
		return self.__tamanho_quarto
	
	@tamanho_quarto.setter
	def tamanho_quarto(self,tamanho_quarto):
		self.__tamanho_quarto = tamanho_quarto
	
	@property
	def quantidade_camas(self):
		return self.__quantidade_camas
	
	@quantidade_camas.setter
	def quantidade_camas(self,quantidade_camas):
		self.__quantidade_camas = quantidade_camas

	@property
	def jacuzzi(self):
		return self.__jacuzzi
	
	@jacuzzi.setter
	def jacuzzi(self,jacuzzi):
		self.__jacuzzi = jacuzzi