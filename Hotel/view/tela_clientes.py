from queue import Empty


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

    def mostra_excluido(self, cliente):
        if cliente is True:
            print('Cliente excluido com sucesso')
            return

        self.reclama_cliente()

    def pega_cliente_por_cpf(self):
        cpf_cliente = input('Digite o CPF do cliente: ')
        return cpf_cliente

    def mostra_cliente_por_cpf(self, cliente):
        print(20 * '*')
        print('Cliente encontrado!')
        print(20 * '*')
        print(f'Nome: {cliente.nome}')
        print(f'Data de nascimento: {cliente.data_nascimento}')
        print(f'CPF: {cliente.cpf}')
        print(f'Email: {cliente.email}')
        print(f'Fone: {cliente.telefone}')
        print(20 * '*')

    def mostra_cliente(self, dados_cliente):
        print(20 * '*')
        print(f"Nome : {dados_cliente['nome_cliente']}")
        print(f"Data de Nascimento : {dados_cliente['data_nascimento_cliente']}")
        print(f"CPF : {dados_cliente['cpf_cliente']}")
        print(f"Email : {dados_cliente['email_cliente']}")
        print(f"Fone : {dados_cliente['fone_cliente']}")
        print(20 * '*')
    
    def cliente_removido(self):
        print(20 * '*')
        print('Cliente removido!')
        print(20 * '*')

    def sem_cliente_cadastrado(self):
        print(20 * '*')
        print('Sem clientes cadastrados!')
        print(20 * '*')

    def cliente_não_encontrado(self):
        print(20 * '*')
        print('Cliente não encontrado!')
        print(20 * '*')