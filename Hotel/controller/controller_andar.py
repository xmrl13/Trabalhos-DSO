from model.andar import Andar
from view.tela_andar import TelaAndar
class ControllerAndar:
	def __init__(self, controller_principal):
		self.__tela_andar = TelaAndar()
		self.__controller_princioal = controller_principal
		self.__andar = []
	
	def inclui_andar(self):
		dados_andar = self.__tela_andar.pega_dados_andar()
		self.__andar.append(Andar(dados_andar))
	
	def altera_andar(self):
		pass
    
	def excluir_andar(self):
		pass
	
	def lista_andar(self):
		if not self.__andar:
			self.__tela_andar.sem_andar_cadastrado()
			return None

		for andar in self.__andar:
			dados_andar = andar.numero
			self.__tela_andar.mostra_andar(dados_andar)

	def retornar(self):
		self.__controller_princioal.abre_tela()

	def abre_tela(self):
		lista_opcoes = {1: self.inclui_andar, 2: self.altera_andar, 3: self.excluir_andar,
			4: self.lista_andar, 0: self.retornar}

		while True:
			opcao = self.__tela_andar.abre_tela()
			lista_opcoes[opcao]()