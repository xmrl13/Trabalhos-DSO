from re import M
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
        lista_com_dicionario_mobilia = dados_quarto['mobilias']
        mobilias = []
        self.__quartos.append(Quarto(dados_quarto['numero_do_quarto'], dados_quarto['valor_da_diaria']))
        for quarto in self.__quartos:
            if dados_quarto['numero_do_quarto'] == quarto.numero_do_quarto:
                for dicionario_de_mobilia in lista_com_dicionario_mobilia:
                    self.__quarto.__mobilias.append(Mobilia(dicionario_de_mobilia['descricao'], dicionario_de_mobilia['quantidade'])) #Criando a lista de mobilias

        
        
        print(mobilias)
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