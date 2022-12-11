import PySimpleGUI as sg

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
        valida_nome = nome_cliente.isalpha()
        if not valida_nome:
            print('')
            print("DIGITE O NOME SOMENTE COM LETRAS!")
            return None

        data_nascimento_cliente = input('Data de nascimento do cliente: ')
        
        cpf_cliente = input('CPF do cliente: ')
        valida_cpf = cpf_cliente.isnumeric()
        if not valida_cpf:
            print("DIGITE O CPF SOMENTE COM NUMEROS")
            return None
            
        email_cliente = input('Email do cliente: ')
        fone_cliente = input('Telefone do cliente: ')
        valida_fone = fone_cliente.isnumeric()
        if not valida_fone:
            print('DIGITE O TELEFONE SOMENTE COM NUMEROS!')
            return None

        

        return {
            'nome_cliente': nome_cliente,
            'data_nascimento_cliente': data_nascimento_cliente,
            'cpf_cliente': cpf_cliente,
            'email_cliente': email_cliente,
            'fone_cliente': fone_cliente
            }

    def pega_cliente_por_cpf(self):
        cpf_cliente = input('Digite o CPF do cliente que deseja buscar: ')
        valida_cpf_cliente = cpf_cliente.isnumeric()
        if not valida_cpf_cliente:
            print('DIGITE APENAS NÚMEROS PARA O CPF!')
            return None
            
        return cpf_cliente

    def mostra_cliente(self, cliente):
        string = (f'Nome do Cliente: {cliente.nome} \nData de Nascimento: {cliente.data_nascimento} \nCPF: {cliente.cpf} \nEmail: {cliente.email} \nTelefone: {cliente.telefone}')
        sg.Popup('-------Clientes cadastrados no sistema-------', string)
    
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

    def cliente_ja_cadastrado(self):
        print(20 * '*')
        print('Esse cpf já está cadastrado!')
        print(20 * '*')