
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
        quarto = Quarto(dados_quarto['numero_do_quarto'], dados_quarto['valor_da_diaria'])

        for dicionario_de_mobilia in lista_com_dicionario_mobilia:
               quarto.add_mobilia(dicionario_de_mobilia['descricao'], dicionario_de_mobilia['quantidade'])
        self.__quartos.append(quarto)


    def altera_quarto(self):
        pass

    def excluir_quarto(self):
        if self.lista_quartos is None:
            return
        quarto = self.busca_quarto_por_numero()
        if quarto in self.__quartos:
            self.__quartos.remove(quarto)
            self.__tela_quarto.quarto_excluido()
            self.lista_quartos()

    def busca_quarto_por_numero(self):
        numero_do_quarto = self.__tela_quarto.pega_quarto_por_numero()
        for quarto in self.__quartos:
            if numero_do_quarto == quarto.numero_do_quarto:
                return quarto
    
    def lista_quartos(self):
        if not self.__quartos:
            self.__tela_quarto.sem_quartos_cadastrados()
            return None
        
        for quarto in self.__quartos:
            dados_quarto = {
                'numero_do_quarto': quarto.numero_do_quarto,
                'valor_diaria': quarto.valor_diaria,
                'descricao': quarto.mobilias
            }
            self.__tela_quarto.mostra_quartos(dados_quarto)
            

    
    def retornar(self):
        self.__controller_principal.abre_tela()

    
    def abre_tela(self):
        lista_opcoes = {
            1: self.inclui_quarto,
            2: self.altera_quarto,
            3: self.excluir_quarto,
            4: self.busca_quarto_por_numero,
            5: self.lista_quartos,
            0: self.retornar
        }
        while True:
            lista_opcoes[self.__tela_quarto.abre_tela()]()