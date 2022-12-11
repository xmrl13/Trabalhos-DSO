
from view.tela_quarto import TelaQuarto
from model.mobilia import Mobilia
from model.quarto import Quarto
from DAO.quarto_dao import QuartoDao


class ControllerQuarto:
    def __init__(self, controller_principal):
        self.__controller_principal = controller_principal
        self.__tela_quarto = TelaQuarto()
        self.__quarto_dao = QuartoDao()

    def inclui_quarto(self):
        dados_quarto = self.__tela_quarto.pega_dados_quarto()
        
        if dados_quarto is None:
            return

        lista_com_dicionario_mobilia = dados_quarto['mobilias']
        quarto = Quarto(dados_quarto['numero_do_quarto'],
                        dados_quarto['valor_da_diaria'])

        for dicionario_de_mobilia in lista_com_dicionario_mobilia:
            quarto.add_mobilia(dicionario_de_mobilia['descricao'], dicionario_de_mobilia['quantidade'])
            
        self.__quarto_dao.add(quarto)

    def retorna_reservas(self, quarto):
        if quarto in self.__quarto_dao.get_all():
            return quarto.dias_reservados

    def excluir_quarto(self):
        
        if self.__quarto_dao is None:
            return

        quarto_recebido = self.__tela_quarto.pega_quarto_por_numero()
        for quarto in self.__quarto_dao.get_all():
            if quarto.numero_do_quarto == quarto_recebido:
                self.__quarto_dao.remove(quarto.numero_do_quarto)
                self.__controller_principal.controller_andar.excluir_quarto_do_andar(quarto)
                self.__tela_quarto.quarto_excluido()
                self.__quarto_dao.save()
                self.lista_quartos()
                return
        self.__tela_quarto.sem_quartos_cadastrados()

    def busca_quarto_por_numero(self):
        if not self.__quarto_dao:
            self.__tela_quarto.sem_quartos_cadastrados()
            return None
        numero_do_quarto = self.__tela_quarto.pega_quarto_por_numero()
        
        for quarto in self.__quarto_dao.get_all():
            if numero_do_quarto == quarto.numero_do_quarto:
                dados_quarto = {
                    'mobilias': quarto.mobilias,
                }
                self.__tela_quarto.mostra_quartos(quarto, dados_quarto)
                return quarto
        self.__tela_quarto.sem_quartos_cadastrados()

    def lista_quartos(self):
        if not self.__quarto_dao:
            self.__tela_quarto.sem_quartos_cadastrados()
            return None

        for quarto in self.__quarto_dao.get_all():            
            dados_quarto = {
                'numero_do_quarto': quarto.numero_do_quarto,
                'mobilias': quarto.mobilias
            }
            self.__tela_quarto.mostra_quartos(quarto, dados_quarto)

    def adiciona_reserva(self, quarto, intervalo_reservado):
        quarto.adiciona_reserva(intervalo_reservado)

    def retornar(self):
        self.__controller_principal.abre_tela()

    def retorna_quartos(self):
        return self.__quarto_dao.get_all()

    def abre_tela(self):
        
        lista_opcoes = {
            1: self.inclui_quarto,
            2: self.excluir_quarto,
            3: self.busca_quarto_por_numero,
            4: self.lista_quartos,
            0: self.retornar
        }
        #try:
        while True:
            lista_opcoes[self.__tela_quarto.abre_tela()]()

        #except Exception:
            #self.__tela_quarto.opcao_invalida()
            #self.abre_tela()


