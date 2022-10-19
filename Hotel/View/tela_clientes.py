

class TelaCliente:
    def mostra_tela_opcoes(self):
        print(20 * '*')
        print(' CLIENTES ')
        print(20 * '*')
        print('1 - Cadastrar Cliente')
        print('2 - Alterar Cliente')
        print('3 - Remover Cliente')
        print('4 - Alterar Cliente')
        print('0 - Voltar')
        # É necessario revisar se este try except esta correto
        try:
            opcao = int(input('Digite uma opção: '))
            return opcao
        except:
            print('Opcão inválida! ')
            opcao = int(input('Tente novamente com uma opção válida: '))
            return opcao
        
    def pega_dados_cliente(self):
        print('CADASTRO DO CLIENTE')
        nome_cliente = input('Nome do cliente: ')
        fone_cliente = input('Telefone do cliente: ')
        email_cliente = input('Email do cliente: ')
        return {
            'nome_cliente': nome_cliente,
            'fone_cliente': fone_cliente,
            'email_cliente': email_cliente
        }
    
    def mostra_cliente(self, dados_cliente):
        print('CLIENTE')
        print(f"Nome: {dados_cliente['nome_cliente']}")
        print(f"Fone: {dados_cliente['fone_cliente']}")
        print(f"Email: {dados_cliente['email_cliente']}")
        