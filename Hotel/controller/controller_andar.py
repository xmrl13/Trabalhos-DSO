from model.andar import Andar
from view.tela_andar import TelaAndar


class ControllerAndar:
    def __init__(self, controller_principal):
        self.__tela_andar = TelaAndar()
        self.__controller_principal = controller_principal
        self.__andar = []

    def inclui_andar(self):
        quartos = self.__controller_principal.retorna_quartos()
        if not quartos:
            self.__tela_andar.reclama_quartos()
            return

        dados_andar = int(self.__tela_andar.inclui_andar())
        quartos = []
        while True:
            dados_quarto = self.__controller_principal.pega_quartos()

            if dados_quarto:
                quartos.append(dados_quarto)
            resposta = self.__tela_andar.mais_quartos()
            if resposta == 'N':
                break
        self.__andar.append(Andar(dados_andar, quartos))

    def excluir_andar(self):
        andar_a_verificar = int(self.__tela_andar.buscar_andar())
        for andar in self.__andar:
            if andar.numero == andar_a_verificar:
                self.__andar.remove(andar)
                return

        self.__tela_andar.reclama_andar()

    def lista_andar(self):
        if not self.__andar:
            self.__tela_andar.sem_andar_cadastrado()
            return None

        for andar in self.__andar:
            self.__tela_andar.mostra_andar(andar.numero)

            dados_andar = andar.quartos
            for quarto in dados_andar:
                self.__tela_andar.mostra_quarto_do_andar(
                    self.__controller_principal.mostra_quarto(quarto))

    def retornar(self):
        self.__controller_principal.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.inclui_andar, 2: self.excluir_andar,
                        3: self.lista_andar, 0: self.retornar}

        while True:
            opcao = self.__tela_andar.abre_tela()
            lista_opcoes[opcao]()
