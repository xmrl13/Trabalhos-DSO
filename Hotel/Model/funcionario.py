from model.pessoa import Pessoa

class Funcionario(Pessoa):

	def __init__(self, cracha: int):
		super().__init__()
		self.__cracha = cracha
	
	@property
	def cracha(self):
		return self.__cracha
	
	@cracha.setter
	def cracha(self,cracha):
		self.__cracha = cracha
	
