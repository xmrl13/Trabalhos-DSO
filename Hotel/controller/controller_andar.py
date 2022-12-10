from model.andar import Andar
from view.tela_andar import TelaAndar
from DAO.andar_dao import AndarDao


class ControllerAndar:
    def __init__(self, controller_principal):
        self.__tela_andar = TelaAndar()
        self.__controller_principal = controller_principal
        self.__andar_dao = AndarDao()


    def inclui_andar(self):
        dados_andar = self.__tela_andar.inclui_andar()
        if dados_andar is None:
            return

        andar_novo = Andar(dados_andar)
        self.__andar_dao.add(andar_novo)

    def add_quarto_no_andar(self):
        quartos = self.__controller_principal.retorna_quartos()
        if not quartos:
            self.__tela_andar.reclama_quartos()
            return

        quarto = self.__controller_principal.controller_quarto.busca_quarto_por_numero()
        if quarto is None:
            return
        
        andar = self.buscar_andar()
        if not andar:
            return
        else:
            andar.add_quarto(quarto)    

    def buscar_andar(self):
        if not self.__andar_dao:
            self.__tela_andar.sem_andar_cadastrado()
            return

        andar_numero = self.__tela_andar.buscar_andar()
        for andar in self.__andar_dao.get_all():
            if andar.numero == andar_numero:
                self.__tela_andar.mostra_andar(andar.numero)
                if andar.quartos is None:
                    self.__tela_andar.reclama_andar_sem_quarto()
                    return andar

                for quartos in andar.quartos:
                    self.__controller_principal.controller_quarto.mostra_quartos(quartos)
                return andar
        self.__tela_andar.reclama_andar()
        return None    

    def excluir_andar(self):
        if not self.__andar_dao.get_all():
            self.__tela_andar.sem_andar_cadastrado()
            return
        andar_a_verificar = int(self.__tela_andar.buscar_andar())
        if andar_a_verificar is None:
            return

        for andar in self.__andar_dao.get_all():
            if andar.numero == andar_a_verificar:
                self.__andar_dao.remove(andar.numero)
                self.__tela_andar.andar_excluido()
                return

        self.__tela_andar.reclama_andar()

    def lista_andar(self):
        if not self.__andar_dao.get_all():
            self.__tela_andar.sem_andar_cadastrado()
            return None

        for andar in self.__andar_dao.get_all():
            self.__tela_andar.mostra_andar(andar.numero)

            dados_andar = andar.quartos
            for quarto in dados_andar:
                    self.__controller_principal.mostra_quarto(quarto)

    def retornar(self):
        self.__controller_principal.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.inclui_andar, 2:self.add_quarto_no_andar , 3: self.excluir_andar,
                        4: self.lista_andar, 0: self.retornar}
        try:
            while True:
                opcao = self.__tela_andar.abre_tela()
                lista_opcoes[opcao]()
        except Exception:
            self.__tela_andar.opcao_invalida()
            self.abre_tela()
