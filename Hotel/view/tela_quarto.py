
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
			descricao = input("Mobilia: ")
			quantidade = input("Quantidade: ")
			mobilias.append({'descricao': descricao, 'quantidade':quantidade})
		return {
			'numero_do_quarto': numero_do_quarto,
			'valor_da_diaria': valor_da_diaria,
			'mobilias': mobilias
		}
		#  mobilias['descricao'] = quantidade    -> seta no dicionario