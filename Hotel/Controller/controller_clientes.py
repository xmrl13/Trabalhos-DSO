
from view.tela_clientes import TelaCliente
from model.cliente import Cliente

class ControllerClientes:
    def __init__(self, controller_principal):
        self.__controller_principal = controller_principal
        self.__clientes = []
        self.__tela_clientes = TelaCliente

    
    def inclui_cliente(self):
        dados_cliente = self.__tela_clientes.pega_dados_cliente()
        cliente = Cliente(dados_cliente['nome_cliente'],
        dados_cliente['data_nascimento_cliente'],
        dados_cliente['cpf_cliente'],
        dados_cliente['email_cliente'],
        dados_cliente['fone_cliente'])

    def altera_cliente(self):
        ...
    
    def excluir_cliente(self):
        ...

    def busca_cliente(self, cpf): #get cliente by CPF
        for cliente in self.__clientes:
            if cliente.cpf_cliente == cpf:
                return cliente
    
    def lista_cliente(self):
        for cliente in self.__clientes:
            dados_cliente = {
                'nome_cliente': cliente.nome_cliente,
                'data_nascimento_cliente': cliente.data_nascimento_,
                'cpf_cliente': cliente.cpf_cliente,
                'email_cliente': cliente.email_cliente,
                'fone_cliente': cliente.fone_cliente
            }
            self.__tela_clientes.mostra_cliente(dados_cliente)
    
    def mostra_tela_opcoes(self):
        opcoes = {
                1: self.inclui_cliente,
                2: self.altera_cliente,
                3: self.excluir_cliente,
                4: self.busca_cliente
            }
        while True:
            opcao = self.__tela_clientes.mostra_tela_opcoes()
            if opcao == 0:
                break
            opcoes[opcao]()