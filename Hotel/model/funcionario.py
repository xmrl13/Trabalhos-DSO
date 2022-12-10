from Hotel.model.pessoa import Pessoa

class Funcionario(Pessoa):

	def __init__(self, nome: str, data_nascimento: str, cracha: int):
		super().__init__(nome, data_nascimento)
		self.__cracha = cracha
	
	@property
	def cracha(self):
		return self.__cracha
	
	@cracha.setter
	def cracha(self,cracha):
		self.__cracha = cracha
	
