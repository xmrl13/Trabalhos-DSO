from view.tela_funcionarios import TelaFuncionarios
from model.funcionario import Funcionario
from DAO.funcionario_dao import FuncionarioDao

class ControllerFuncionarios:
    def __init__(self, controller_principal):
        self.__controller_principal = controller_principal
        self.__tela_funcionarios = TelaFuncionarios()
        self.__funcionario_dao = FuncionarioDao()

    def inclui_funcionario(self):
        resposta, dados_funcionario = self.__tela_funcionarios.pega_dados_funcionario()
        if resposta == 'salvar':
            if dados_funcionario == None:
                return
            print(dados_funcionario)

            funcionarios = self.__funcionario_dao.get_all()
            print(funcionarios)

            funcionario_criado = Funcionario(dados_funcionario['nome_funcionario'],
                                                   dados_funcionario['data_nascimento_funcionario'],
                                                  dados_funcionario['cracha_do_funcionario'])

            self.__funcionario_dao.add(funcionario_criado)

    def altera_funcionario(self):
        numero_cracha = self.__tela_funcionarios.pega_funcionario_por_cracha()
        if numero_cracha == None:
            return
        for funcionario in self.__funcionarios:
            if funcionario.cracha == numero_cracha:
                funcionario_atualizado = self.__tela_funcionarios.altera_funcionario()
                funcionario.nome = funcionario_atualizado['nome_funcionario']
                funcionario.data_nascimento = funcionario_atualizado['data_nascimento_funcionario']
                funcionario.cracha = funcionario_atualizado['cracha_do_funcionario']
                self.__tela_funcionarios.confirma_funcionario()
                return
        self.__tela_funcionarios.reclama_funcionario()

    def excluir_funcionario(self):
        numero_cracha = self.__tela_funcionarios.pega_funcionario_por_cracha()
        if numero_cracha == None:
            return

        for funcionario in self.__funcionarios:
            if funcionario.cracha == numero_cracha:
                self.__funcionarios.remove(funcionario)
                self.__tela_funcionarios.confirma_funcionario()
                return

        self.__tela_funcionarios.reclama_funcionario()

    def busca_funcionario(self):
        numero_cracha = self.__tela_funcionarios.pega_funcionario_por_cracha()
        if numero_cracha == None:
            return None

        for funcionario in self.__funcionarios:
            if funcionario.cracha == numero_cracha:
                dados_funcionario = {
                    'nome_funcionario': funcionario.nome,
                    'data_nascimento_funcionario': funcionario.data_nascimento,
                    'numero_do_cracha': funcionario.cracha
                }
                self.__tela_funcionarios.mostra_funcionario(dados_funcionario)
                return dados_funcionario

        self.__tela_funcionarios.reclama_funcionario()
        return None

    def lista_funcionario(self):
        if not self.__funcionario_dao.get_all():
            self.__tela_funcionarios.sem_funcionarios_cadastrados()
            return 

        if self.__funcionario_dao.get_all() is None:
            self.__tela_funcionarios.reclama_funcionario()
            return
            
        for funcionario in self.__funcionario_dao.get_all():
            dados_funcionario = {
                'data_nascimento_funcionario': funcionario.data_nascimento,
                'nome_funcionario': funcionario.nome,
                'numero_do_cracha': funcionario.cracha
            }
            self.__tela_funcionarios.mostra_funcionario(dados_funcionario)

    def retornar(self):
        self.__controller_principal.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.inclui_funcionario,
            2: self.altera_funcionario,
            3: self.excluir_funcionario,
            4: self.busca_funcionario,
            5: self.lista_funcionario,
            0: self.retornar
        }
        #try:
        while True:
            lista_opcoes[self.__tela_funcionarios.abre_tela()]()

        #except Exception:
            '''self.__tela_funcionarios.opcao_invalida()
            self.abre_tela()'''
