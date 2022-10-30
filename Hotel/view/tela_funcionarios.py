

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
        print("5 - Listar funcionarios")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))

        return opcao

    def pega_funcionario_por_cracha(self):
        cracha_funcionario = input(
            'Digite o Numero de cracha do funcionario: ')
        verifica_cracha = cracha_funcionario.isnumeric()
        if not verifica_cracha:
            print()
            print('DIGITE SOMENTE NUMEROS PARA BUSCAR O CRACHA')
            return None
        
        cracha_funcionario = int(cracha_funcionario)
        return cracha_funcionario

    def pega_dados_funcionario(self):
        print('CADASTRO DO FUNCIONARIO')
        nome_funcionario = (input('Nome do Funcionario: '))
        verifica_nome_funcionario = nome_funcionario.isalpha()
        if not verifica_nome_funcionario:
            print()
            print('DIGITE SOMENTE LETRAS PARA CADASTRAR FUNCIONARIO')
            return None

        data_nascimento_funcionario = input(
            'Data de nascimento do Funcionario: ')
        cracha = input('Numero de cracha do Funcionario: ')
        verifica_cadastro =cracha.isnumeric()
        if not verifica_cadastro:
            print()
            print('DIGITE SOMENTE NUMEROS PARA CADASTRAR CRACHA')
            return None
        cracha = int(cracha)

        return {
            'nome_funcionario': nome_funcionario,
            'data_nascimento_funcionario': data_nascimento_funcionario,
            'cracha_do_funcionario': cracha
        }
    
    def altera_funcionario(self):
        print('ALTERAR DADOS DO FUNCIONARIO')
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
        print(f"Cracha : {dados_funcionario['numero_do_cracha']}")
        print(20 * '*')

    def reclama_funcionario(self):
        print(20 * '*')
        print('FUNCIONARIO NAO ENCONTRADO')
        print(20 * '*')
    
    def confirma_funcionario(self):
        print(20 * '*')
        print('ALTERAÇAO FEITA COM SUCESSO')
        print(20 * '*')
    
    def opcao_invalida(self):
        print(20 * '*')
        print('POR FAVOR DIGITE UM VALOR NÚMERICO E DENTRO DO INTERVALO VÁLIDO!')
        print(20 * '*')
    
    def funcionario_exitente(self):
        print(20 * '*')
        print('Funcionario com mesmo numero de cracha já existente')
        print(20 * '*')

    def sem_funcionarios_cadastrados(self):
        print('Sem funcionarios cadastrados!')
        