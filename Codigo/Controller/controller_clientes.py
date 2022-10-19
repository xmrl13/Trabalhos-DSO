from controller_principal import ControllerPrincipal
from View.tela_clientes import TelaCliente
from Model.cliente import   Cliente

class ControllerClientes:
    def __init__(self, controller_principal):
        self.__controller_principal = controller_principal
        self.__clientes = []
        self.__tela_clientes = TelaCliente

    
    def inclui_cliente(self):
        dados_cliente = self.__tela_clientes.pega_dados_cliente()
        cliente = Cliente(dados_cliente['nome_cliente']
        )

    def altera_cliente(self):
        ...
    
    def excluir_cliente(self):
        ...

    def busca_cliente(self): #get cliente by CPF
        ...