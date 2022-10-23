from model.tipo_quarto import TipoQuarto
from view.tela_tipo_quarto import TelaTipoQuarto


class ControllerTipoQuarto:
    def __init__(self, controller_principal):
        self.__controller_principal = controller_principal
        self.__tela_tipo_quarto = TelaTipoQuarto()
        self.__tipos_quartos = []

    def inclui_tipos_quarto(self):
        dados_tipo_quarto = self.__tela_tipo_quarto.pega_dados_tipo_quarto()
        self.__tipos_quartos.append(TipoQuarto(
            dados_tipo_quarto['tamanho_quarto'], dados_tipo_quarto['quantidade_camas'], dados_tipo_quarto['jacuzzi']))

    def altera_tipos_quarto(self):
        tamanho = self.__tela_tipo_quarto.pega_quarto_por_tamanho()
        for quarto in self.__tipos_quartos:
            if quarto.tamanho_quarto == tamanho:
                tipo_quarto_atualizado = self.__tela_tipo_quarto.altera_tipo_quarto()
                quarto.tamanho_quarto = tipo_quarto_atualizado['tamanho_quarto']
                quarto.quantidade_camas = tipo_quarto_atualizado['quantidade_camas']
                quarto.jacuzzi = tipo_quarto_atualizado['jacuzzi']
                self.__tela_tipo_quarto.confirma_tipo_quarto()
                return
        self.__tela_tipo_quarto.reclama_tipo_quarto()

    def excluir_tipos_quarto(self):
        tamanho = self.__tela_tipo_quarto.pega_quarto_por_tamanho()
        for quarto in self.__tipos_quartos:
            if quarto.tamanho_quarto == tamanho:
                self.__tipos_quartos.remove(quarto)
                self.__tela_tipo_quarto.confirma_tipo_quarto()
                return

        self.__tela_tipo_quarto.reclama_tipo_quarto()

    def busca_tipos_quarto(self):
        tamanho = self.__tela_tipo_quarto.pega_quarto_por_tamanho()
        for quarto in self.__tipos_quartos:
            if quarto.tamanho_quarto == tamanho:
                dados_quarto = {
                    'tamanho_quarto': quarto.tamanho_quarto,
                    'quantidade_camas': quarto.quantidade_camas,
                    'jacuzzi': quarto.jacuzzi
                }
                self.__tela_tipo_quarto.mostra_tipo_quarto(dados_quarto)
                return

        self.__tela_tipo_quarto.reclama_tipo_quarto()

    def lista_tipos_quarto(self):
        for tipo_quarto in self.__tipos_quartos:
            dados_tipo_quarto = {
                'tamanho_quarto': tipo_quarto.tamanho_quarto,
                'quantidade_camas': tipo_quarto.quantidade_camas,
                'jacuzzi': tipo_quarto.jacuzzi
            }
            self.__tela_tipo_quarto.mostra_tipo_quarto(dados_tipo_quarto)

    def retornar(self):
        self.__controller_principal.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.inclui_tipos_quarto,
            2: self.altera_tipos_quarto,
            3: self.excluir_tipos_quarto,
            4: self.busca_tipos_quarto,
            5: self.lista_tipos_quarto,
            0: self.retornar
        }
        while True:
            lista_opcoes[self.__tela_tipo_quarto.abre_tela()]()
