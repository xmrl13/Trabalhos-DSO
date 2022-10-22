
from queue import Empty
from model import cliente
from model.pessoa import Pessoa
from view.tela_clientes import TelaCliente
from model.cliente import Cliente

class ControllerClientes:
    def __init__(self, controller_principal):
        self.__controller_principal = controller_principal
        self.__tela_clientes = TelaCliente()
        self.__clientes = []

    
    def inclui_cliente(self):
        dados_cliente = self.__tela_clientes.pega_dados_cliente()
        self.__clientes.append(Cliente(dados_cliente['nome_cliente'],
        dados_cliente['data_nascimento_cliente'],
        dados_cliente['cpf_cliente'],
        dados_cliente['email_cliente'],
        dados_cliente['fone_cliente']))


    def altera_cliente(self):
        ...
    
    def excluir_cliente(self):
        cliente = self.busca_cliente_por_cpf()
        for cliente in self.__clientes:
            if cliente in self.__clientes:
                self.__clientes.remove(cliente)
                self.__tela_clientes.mostra_excluido(True)
            else: 
                self.__tela_clientes.reclama_cliente()

    def busca_cliente_por_cpf(self): #get cliente by CPF
        cpf = self.__tela_clientes.pega_cliente_por_cpf()
        for cliente in self.__clientes:
            if cpf == cliente.cpf:
                self.__tela_clientes.mostra_cliente_por_cpf(cliente)
                return
            self.__tela_clientes.reclama_cliente()


    def retornar(self):
        self.__controller_principal.abre_tela()

    def lista_cliente(self):
        if not self.__clientes:
            print('Sem clientes cadastrados') # Tem que tirar esse print daqui

        for cliente in self.__clientes:
                dados_cliente = {
            'data_nascimento_cliente': cliente.data_nascimento,
            'nome_cliente': cliente.nome,
            'cpf_cliente': cliente.cpf,
            'email_cliente': cliente.email,
            'fone_cliente': cliente.telefone
        }
                self.__tela_clientes.mostra_cliente(dados_cliente)
    
    def abre_tela(self):
        lista_opcoes = {1: self.inclui_cliente, 2: self.altera_cliente, 3: self.excluir_cliente,
         4: self.busca_cliente_por_cpf, 5: self.lista_cliente, 0: self.retornar}

        while True:
            opcao = self.__tela_clientes.abre_tela()
            lista_opcoes[opcao]()


'''
Classe enum para tipos de quartos
'''