from controller.controller_clientes import ControllerClientes
class TelaCliente:

    def abre_tela(self):
        print(20 * '*')
        print(' CLIENTES ')
        print(20 * '*')
        print('1 - Cadastrar Cliente')
        print('2 - Alterar Cliente')
        print('3 - Remover Cliente')
        print('4 - Busca Cliente')
        print('5 - Lista Cliente')
        print('0 - Voltar')
        opcao = int(input('Digite uma opção: '))
        return opcao

    def pega_dados_cliente(self):
        print('CADASTRO DO CLIENTE')
        nome_cliente = input('Nome do cliente: ')
        data_nascimento_cliente = input('Data de nascimento do cliente: ')
        cpf_cliente = input('CPF do cliente: ')
        email_cliente = input('Email do cliente: ')
        fone_cliente = input('Telefone do cliente: ')
        return {
            'nome_cliente': nome_cliente,
            'data_nascimento_cliente': data_nascimento_cliente,
            'cpf_cliente': cpf_cliente,
            'email_cliente': email_cliente,
            'fone_cliente': fone_cliente
        }
    
    def mostra_cliente_por_cpf(self):
        print(20 * '*')
        print('BUSCA DE CLIENTE PELO CPF!')
        print(20 * '*')
        cpf_cliente = input('Digite o CPF do cliente a ser localizado: ')

        return cpf_cliente

    def mostra_cliente(self, dados_cliente):
        print(20 * '*')
        print(f"Nome : {dados_cliente['nome_cliente']}")
        print(f"Data de Nascimento : {dados_cliente['data_nascimento_cliente']}")
        print(f"CPF : {dados_cliente['cpf_cliente']}")
        print(f"Email : {dados_cliente['email_cliente']}")
        print(f"Fone : {dados_cliente['fone_cliente']}")
        print(20 * '*')
