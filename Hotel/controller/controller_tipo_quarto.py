from model.tipo_quarto import TipoQuarto
from view.tela_tipo_quarto import TelaTipoQuarto

class ControllerTipoQuarto:
    def __init__(self, controller_principal):
        self.__controller_principal = controller_principal
        self.__tela_tipo_quarto = TelaTipoQuarto
        self.__tipos_quartos = []

    def inclui_tipos_quarto(self):

        pass

    def altera_tipos_quarto(self):
        pass
    
    def excluir_tipos_quarto(self):
        pass

    def busca_tipos_quarto(self):
        pass
    
    def lista_tipos_quarto(self):
        pass

    def retornar(self):
        self.__controller_principal.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.inclui_tipos_quarto, 2: self.altera_tipos_quarto, 3: self.excluir_tipos_quarto,
            4: self.busca_tipos_quarto, 5: self.lista_tipos_quarto, 0: self.retornar
        }
        while True:
            lista_opcoes[self.__tela_tipo_quarto.abre_tela()]()