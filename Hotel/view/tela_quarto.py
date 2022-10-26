
class TelaQuarto:

	def abre_tela(self):
		print(20 * '*')
		print("QUARTOS")
		print(20 * '*')
		print(" Escolha a opçao ")
		print("1 - Incluir Quarto")
		print("2 - Alterar Quarto")
		print("3 - Excluir Quarto")
		print("4 - Busca Quarto")
		print("5 - Mostra Quarto")
		print("0 - Retornar")
		opcao = int(input("Escolha a opcao: "))
		return opcao

        	

	def pega_dados_quarto(self):
		print('CADASTRO DO QUARTO')
		numero_do_quarto = input('Numero do quarto: ')
		valor_da_diaria = input('Valor da diaria: ')
		mobilias = []
		while True:
			rest = input('deseja incluir mobilia? [S/N]').upper()
			if rest == 'N':
				break
			descricao = input("Descrição da mobilia: ")
			quantidade = int(input("Quantidade: "))
			mobilias.append({'descricao': descricao, 'quantidade':quantidade})
		return {
			'numero_do_quarto': numero_do_quarto,
			'valor_da_diaria': valor_da_diaria,
			'mobilias': mobilias
		}
	
	def pega_quarto_por_numero(self):
		numero_do_quarto = input('Digite o numero do quarto que deseja localizar: ')
		return numero_do_quarto

	def sem_quartos_cadastrados(self):
		print('Sem quartos cadastrados!')
	
	def quarto_excluido(self):
		print(20 * '*')
		print('Quarto excluido com sucessso')
		print(20 * '*')

	def mostra_quartos(self, dados_quarto):
		print(20 * '*')
		print(f"Numero do quarto: {dados_quarto['numero_do_quarto']}")
		print(f"Valor da diária: {dados_quarto['valor_diaria']}")
		print(f"Mobilias: {dados_quarto['descricao']}")