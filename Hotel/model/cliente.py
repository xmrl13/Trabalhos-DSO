from datetime import date, datetime
from model.pessoa import Pessoa

class Cliente(Pessoa):

	def __init__(self, nome: str, data_nascimento: str , cpf: str, e_mail: str, telefone:str):
		super().__init__(nome, data_nascimento)
		self.__cpf = cpf
		self.__e_mail = e_mail
		self.__telefone = telefone

	@property
	def cpf(self):
		return self.__cpf 

	@cpf.setter
	def cpf(self,cpf):
		self.__cpf = cpf
	
	@property
	def e_mail(self):
		return self.__e_mail

	@e_mail.setter
	def e_mail(self,e_mail):
		self.__e_mail = e_mail
	
	@property
	def telefone(self):
		return self.__telefone 

	@telefone.setter
	def telefone(self,telefone):
		self.__telefone = telefone
