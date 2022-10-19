from controller_principal import ControllerPrincipal
from View.tela_funcionarios import TelaFuncionarios


class ControllerFuncionarios:
    def __init__(self, controller_principal):
        self.__controller_principal = controller_principal
        self.__tela_funcionarios = TelaFuncionarios()
        self.__funcionarios = []
        

    def inclui_funcionario(self):
        pass

    def altera_funcionario(self):
        pass

    def excluir_funcionario(self):
        pass

    def busca_funcionario(self):
        pass

    def retornar(self):
        self.__controller_principal.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {
            1: self.inclui_funcionario, 
            2: self.altera_funcionario, 
            3: self.excluir_funcionario, 
            4: self.busca_funcionario, 
            0: self.retornar
        }
        while True:
            lista_opcoes[self.__tela_funcionarios.tela_opcoes()]()