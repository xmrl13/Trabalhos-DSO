

class TelaCliente:

    def abre_tela(self):
        print(20 * '*')
        print(5 * '-', 'Clientes', 5 * '-')
        print(20 * '*')
        print('1 - Cadastrar Cliente')
        print('2 - Alterar dados do Cliente')
        print('3 - Remover Cliente')
        print('4 - Buscar Cliente por CPF')
        print('5 - Listar Clientes')
        print('0 - Voltar')
        opcao = int(input('Digite uma opção: '))
        return opcao

    def pega_dados_cliente(self):
        print('Insira os dados do Cliente')
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

    def pega_cliente_por_cpf(self):
        cpf_cliente = input('Digite o CPF do cliente que deseja buscar: ')
        return cpf_cliente

    def mostra_cliente(self, dados_cliente):
        print(20 * '*')
        print(f"Nome : {dados_cliente['nome_cliente']}")
        print(f"Data de Nascimento : {dados_cliente['data_nascimento_cliente']}")
        print(f"CPF : {dados_cliente['cpf_cliente']}")
        print(f"Email : {dados_cliente['email_cliente']}")
        print(f"Fone : {dados_cliente['fone_cliente']}")
        print(20 * '*')
    
    def cliente_alterado(self):
        print(20 * '*')
        print('Cliente alterado com sucesso!')
        print(20 * '*')


    def cliente_encontrado(self):
        print(20 * '*')
        print('Cliente encontrado!')
        print(20 * '*')

    def cliente_removido(self):
        print(20 * '*')
        print('Cliente removido com sucesso!')
        print(20 * '*')

    def sem_cliente_cadastrado(self):
        print(20 * '*')
        print('Sem clientes cadastrados!')
        print(20 * '*')

    def cliente_não_encontrado(self):
        print(20 * '*')
        print('Cliente não encontrado!')
        print(20 * '*')

    def opcao_invalida(self):
        print(20 * '*')
        print('POR FAVOR DIGITE UM VALOR NÚMERICO E DENTRO DO INTERVALO VÁLIDO!')
        print(20 * '*')
