from view.tela_quarto import TelaQuarto
from model.mobilia import Mobilia
from model.quarto import Quarto

class ControllerQuarto:
    def __init__(self, controller_principal):
        self.__controller_principal = controller_principal
        self.__tela_quarto = TelaQuarto()
        self.__quartos = []

    def inclui_quarto(self):

        pass

    def altera_quarto(self):
        pass

    def excluir_quarto(self):
        pass

    def busca_quarto(self):
        pass
    

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
            lista_opcoes[self.__tela_quarto.abre_tela()]()