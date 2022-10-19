from abc import ABC, abstractmethod
from datetime import date

class Pessoa(ABC):

	@abstractmethod
	def __init__(self, nome : str, data_nascimento: date):
		self.__nome = nome
		self.__data_nascimento = data_nascimento
		
	@property
	def nome(self):
		return self.__nome
	
	@nome.setter
	def nome(self,nome):
		self.__nome = nome
	
	@property
	def data(self):
		return self.__data_nascimento
	
	@nome.setter
	def nome(self,data_nascimento):
		self.__data_nascimento = data_nascimento
	

	
		
