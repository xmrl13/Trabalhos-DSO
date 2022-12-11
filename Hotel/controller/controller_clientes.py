from model import cliente
from model.pessoa import Pessoa
from view.tela_clientes import TelaCliente
from model.cliente import Cliente
from DAO.cliente_dao import ClienteDao

class ControllerClientes:
    def __init__(self, controller_principal):
        self.__controller_principal = controller_principal
        self.__tela_clientes = TelaCliente()
        self.__cliente_dao = ClienteDao()

    
    def inclui_cliente(self):
        dados_cliente = self.__tela_clientes.pega_dados_cliente()
        if dados_cliente == None:
            return
                
        cliente_criado = Cliente(dados_cliente['nome_cliente'],
        dados_cliente['data_nascimento_cliente'],
        dados_cliente['cpf_cliente'],
        dados_cliente['email_cliente'],
        dados_cliente['fone_cliente'])

        for cliente in self.__cliente_dao.get_all():
            if dados_cliente['cpf_cliente'] == cliente.cpf:
                self.__tela_clientes.cliente_ja_cadastrado()
                return

        self.__cliente_dao.add(cliente_criado)


    def altera_cliente(self):

        cliente = self.busca_cliente_por_cpf()

        for cliente_loop in self.__cliente_dao.get_all():
            if cliente_loop.cpf == cliente.cpf:
                novos_dados = self.__tela_clientes.pega_dados_cliente()
                cliente.nome = novos_dados['nome_cliente']
                cliente.data_nascimento = novos_dados['data_nascimento_cliente']
                cliente.cpf = novos_dados['cpf_cliente']
                cliente.email_cliente = novos_dados['email_cliente']
                cliente.telefone = novos_dados['fone_cliente']
                self.__cliente_dao.save()
            self.__tela_clientes.cliente_alterado()


    def excluir_cliente(self):
        if not self.__cliente_dao.get_all():
            self.__tela_clientes.sem_cliente_cadastrado()
            return
        cliente_buscado = self.busca_cliente_por_cpf()
        if cliente_buscado is None:
            return

        for cliente in self.__cliente_dao.get_all():
            if cliente_buscado.cpf == cliente.cpf:
                self.__cliente_dao.remove(cliente.cpf)
                self.__tela_clientes.cliente_removido()
                return

    def busca_cliente_por_cpf(self): #get cliente by CPF
        if not self.__cliente_dao.get_all():
            self.__tela_clientes.sem_cliente_cadastrado()
            return None
        cpf = self.__tela_clientes.pega_cliente_por_cpf()
        if cpf == None:
            return
            
        for cliente in self.__cliente_dao.get_all():
            if cpf == cliente.cpf:
                self.__tela_clientes.cliente_encontrado()
                self.__tela_clientes.mostra_cliente(cliente)
                return cliente
            
        self.__tela_clientes.cliente_não_encontrado()

    def retornar(self):
        self.__controller_principal.abre_tela()

    def lista_cliente(self):
        if not self.__cliente_dao.get_all():
            self.__tela_clientes.sem_cliente_cadastrado()
            return None

        for cliente in self.__cliente_dao.get_all():
            self.__tela_clientes.mostra_cliente(cliente)
            
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
