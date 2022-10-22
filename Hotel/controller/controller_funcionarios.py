from view.tela_funcionarios import TelaFuncionarios
from model.funcionario import Funcionario


class ControllerFuncionarios:
    def __init__(self, controller_principal):
        self.__controller_principal = controller_principal
        self.__tela_funcionarios = TelaFuncionarios()
        self.__funcionarios = []

    def inclui_funcionario(self):
        dados_funcionario = self.__tela_funcionarios.pega_dados_funcionario()
        self.__funcionarios.append(Funcionario(dados_funcionario['nome_funcionario'],
                                               dados_funcionario['data_nascimento_funcionario'],
                                               dados_funcionario['cracha_do_funcionario']))

    def altera_funcionario(self):
        pass

    def excluir_funcionario(self):
        self.lista_funcionario()
        funcionario = self.pega_funcionario_por_cracha()
        if funcionario in self.__funcionarios:
            self.__funcionario.remove(funcionario)
            return
        self.reclama_funcionario()

    def busca_funcionario(self):
        pass

    def lista_funcionario(self):
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
        while True:
            lista_opcoes[self.__tela_funcionarios.abre_tela()]()   
        #
             
