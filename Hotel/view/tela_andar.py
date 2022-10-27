
class TelaAndar:

	def abre_tela(self):
		print(20 * '*')
		print("Andar")
		print(20 * '*')
		print(" Escolha a opçao ")
		print("1 - Incluir Andar")
		print("2 - Alterar Andar")
		print("3 - Excluir Andar")
		print("4 - Lista Andares")
		print("0 - Retornar")
		opcao = int(input("Escolha a opcao: "))
		return opcao
        	

	def pega_dados_andar(self):
		print('Cadastrar Andar')
		numero_andar = input('Numero do andar: ')
		return numero_andar

	def sem_andar_cadastrado(self):
		print('Sem nenhum andar cadastrados!')
	
	def andar_excluido(self):
		print(20 * '*')
		print('Andar excluido com sucessso')
		print(20 * '*')

	def mostra_andar(self, andares):
		print(20 * '*')
		print(f"Andares cadastrados: {andares}º")