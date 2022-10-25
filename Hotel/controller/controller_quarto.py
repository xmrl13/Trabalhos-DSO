from view.tela_quarto import TelaQuarto
from model.mobilia import Mobilia
from model.quarto import Quarto

class ControllerQuarto:
    def __init__(self, controller_principal):
        self.__controller_principal = controller_principal
        self.__tela_quarto = TelaQuarto()
        self.__quartos = []

    def inclui_quarto(self):
        dados_quarto = self.__tela_quarto.pega_dados_quarto()
        mobilia = dados_quarto['mobilias']
        mobilias = {}
        for i, x in mobilia:
            mobilias = {i,x}
            return mobilias
        print(mobilias)

        #self.__quartos.append(Quarto(dados_quarto['numero_do_quarto'], dados_quarto['valor_da_diaria'], Mobilia(dados_quarto['mobilia',['descicao']], dados_quarto['mobilia',['quantidade']])))
        #print(self.__quartos)

    def altera_quarto(self):
        pass

    def excluir_quarto(self):
        pass

    def busca_quarto(self):
        pass
    
    def lista_quarto(self):
        pass
    
    def retornar(self):
        self.__controller_principal.abre_tela()

    
    def abre_tela(self):
        lista_opcoes = {
            1: self.inclui_quarto,
            2: self.altera_quarto,
            3: self.excluir_quarto,
            4: self.busca_quarto,
            5: self.lista_quarto,
            0: self.retornar
        }
        while True:
            lista_opcoes[self.__tela_quarto.abre_tela()]()