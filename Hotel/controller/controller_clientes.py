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
        if cliente is None:
            return
            
        if cliente in self.__cliente_dao.get_all():
                cliente_atualizado = self.__tela_clientes.pega_dados_cliente()
                cliente.nome = cliente_atualizado['nome_cliente']
                cliente.data_nascimento = cliente_atualizado['data_nascimento_cliente']
                cliente.cpf = cliente_atualizado['cpf_cliente']
                cliente.email = cliente_atualizado['email_cliente']
                cliente.telefone = cliente_atualizado['fone_cliente']
                self.__cliente_dao.add(
                    Cliente(cliente_atualizado['nome_cliente'],
                    cliente_atualizado['data_nascimento_cliente'],
                    cliente_atualizado['cpf_cliente'],
                    cliente_atualizado['email_cliente'],
                    cliente_atualizado['fone_cliente']))
                
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
        if not self.__cliente_dao.get_all():
            self.__tela_clientes.sem_cliente_cadastrado()
            return None

        for cliente in self.__cliente_dao.get_all():
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
        except Exception:
            self.__tela_clientes.opcao_invalida()
            self.abre_tela()
 '''