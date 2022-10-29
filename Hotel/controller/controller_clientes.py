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
        cpf = self.__tela_clientes.pega_cliente_por_cpf()
        for cliente in self.__clientes:
            if cpf == cliente.cpf:
                cliente_atualizado = self.__tela_clientes.pega_dados_cliente()
                cliente.nome = cliente_atualizado['nome_cliente']
                cliente.data_nascimento = cliente_atualizado['data_nascimento_cliente']
                cliente.cpf = cliente_atualizado['cpf_cliente']
                cliente.email = cliente_atualizado['email_cliente']
                cliente.telefone = cliente_atualizado['fone_cliente']
                self.__tela_clientes.cliente_alterado()
                return
        self.__tela_clientes.cliente_encontrado()
    
    def excluir_cliente(self):
        if self.lista_cliente is None:
            return
        cliente = self.busca_cliente_por_cpf()
        if cliente in self.__clientes:
            self.__clientes.remove(cliente)
            self.__tela_clientes.cliente_removido()
            return


    def busca_cliente_por_cpf(self): #get cliente by CPF
        if not self.__clientes:
            self.__tela_clientes.sem_cliente_cadastrado()
            return None
        cpf = self.__tela_clientes.pega_cliente_por_cpf()
        for cliente in self.__clientes:
            if cpf == cliente.cpf:
                dados_cliente = {
                    'nome_cliente': cliente.nome,
                    'data_nascimento_cliente': cliente.data_nascimento,
                    'cpf_cliente': cliente.cpf,
                    'email_cliente': cliente.email,
                    'fone_cliente': cliente.telefone
                    }
                self.__tela_clientes.cliente_encontrado()
                self.__tela_clientes.mostra_cliente(dados_cliente)
                return cliente
            
        self.__tela_clientes.cliente_não_encontrado()

    def retornar(self):
        self.__controller_principal.abre_tela()

    def lista_cliente(self):
        if not self.__clientes:
            self.__tela_clientes.sem_cliente_cadastrado()
            return None

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

        try:
            while True:
                opcao = self.__tela_clientes.abre_tela()
                lista_opcoes[opcao]()

        except Exception:
            self.__tela_clientes.opcao_invalida()
            self.abre_tela()

'''
Classe enum para tipos de quartos
'''
 