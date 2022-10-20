from datetime import date, datetime
from model.pessoa import Pessoa

class Cliente(Pessoa):

	def __init__(self, nome: str, data_nascimento: str , cpf: str, email: str, telefone:str):
		super().__init__(nome, data_nascimento)
		self.__cpf = cpf
		self.__email = email
		self.__telefone = telefone

	@property
	def cpf(self):
		return self.__cpf 

	@cpf.setter
	def cpf(self,cpf):
		self.__cpf = cpf
	
	@property
	def email(self):
		return self.__email

	@email.setter
	def email(self,email):
		self.__email = email
	
	@property
	def telefone(self):
		return self.__telefone 

	@telefone.setter
	def telefone(self,telefone):
		self.__telefone = telefone
