from view.tela_funcionarios import TelaFuncionarios
from model.funcionario import Funcionario


class ControllerFuncionarios:
    def __init__(self, controller_principal):
        self.__controller_principal = controller_principal
        self.__tela_funcionarios = TelaFuncionarios()
        self.__funcionarios = []

    def inclui_funcionario(self):
        dados_funcionario = self.__tela_funcionarios.pega_dados_funcionario()
        if dados_funcionario == None:
            return

        for funcionario in self.__funcionarios:
            if funcionario.cracha == dados_funcionario['cracha_do_funcionario']:
                self.__tela_funcionarios.funcionario_exitente()
                return

        self.__funcionarios.append(Funcionario(dados_funcionario['nome_funcionario'],
                                               dados_funcionario['data_nascimento_funcionario'],
                                               dados_funcionario['cracha_do_funcionario']))

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
            return

        for funcionario in self.__funcionarios:
            if funcionario.cracha == numero_cracha:
                dados_funcionario = {
                    'nome_funcionario': funcionario.nome,
                    'data_nascimento_funcionario': funcionario.data_nascimento,
                    'numero_do_cracha': funcionario.cracha
                }
                self.__tela_funcionarios.mostra_funcionario(dados_funcionario)
                return

        self.__tela_funcionarios.reclama_funcionario()

    def lista_funcionario(self):
        if not self.__funcionarios:
            self.__tela_funcionarios.sem_funcionarios_cadastrados()
            return 

        if self.__funcionarios is None:
            self.__tela_funcionarios.reclama_funcionario()
            return
            
        for funcionario in self.__funcionarios:
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
        try:
            while True:
                lista_opcoes[self.__tela_funcionarios.abre_tela()]()

        except Exception:
            self.__tela_funcionarios.opcao_invalida()
            self.abre_tela()
