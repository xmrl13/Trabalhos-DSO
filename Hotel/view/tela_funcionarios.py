

class TelaFuncionarios():
    def abre_tela(self):
        print(20 * '*')
        print("FUNCIONARIOS")
        print(20 * '*')
        print(" Escolha a opçao ")
        print("1 - Incluir funcionario")
        print("2 - Alterar funcionario")
        print("3 - Excluir funcionario")
        print("4 - Busca funcionario")
        print("5 - Mostra funcionarios")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        
        return opcao
	   
		

    def pega_dados_funcionario(self):
        print('CADASTRO DO FUNCIONARIO')
        nome_funcionario = input('Nome do Funcionario: ')
        data_nascimento_funcionario = input(
            'Data de nascimento do Funcionario: ')
        cracha = input('Numero de cracha do Funcionario: ')
        return {
            'nome_funcionario': nome_funcionario,
            'data_nascimento_funcionario': data_nascimento_funcionario,
            'cracha_do_funcionario': cracha
        }

    def mostra_funcionario(self, dados_funcionario):
        print(20 * '*')
        print(f"Nome : {dados_funcionario['nome_funcionario']}")
        print(
            f"Data de Nascimento : {dados_funcionario['data_nascimento_funcionario']}")
        print(f"Cracha : {dados_funcionario['nuumero_do_cracha']}")
        print(20 * '*')
