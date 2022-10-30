
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
        
        if dados_quarto is None:
            return

        lista_com_dicionario_mobilia = dados_quarto['mobilias']
        quarto = Quarto(dados_quarto['numero_do_quarto'],
                        dados_quarto['valor_da_diaria'])

        for dicionario_de_mobilia in lista_com_dicionario_mobilia:
            quarto.add_mobilia(dicionario_de_mobilia['descricao'], dicionario_de_mobilia['quantidade'])
            
        self.__quartos.append(quarto)

    def retorna_reservas(self, quarto):
        if quarto in self.__quartos:
            return quarto.dias_reservados

    def excluir_quarto(self):
        if self.lista_quartos is None:
            return
        quarto_recebido = self.__tela_quarto.pega_quarto_por_numero()
        for quarto in self.__quartos:
            if quarto.numero_do_quarto == quarto_recebido:
                self.__quartos.remove(quarto)
                self.__tela_quarto.quarto_excluido()
                self.lista_quartos()
                return
        self.__tela_quarto.sem_quartos_cadastrados()

    def busca_quarto_por_numero(self):
        if not self.__quartos:
            self.__tela_quarto.sem_quartos_cadastrados()
            return None
        numero_do_quarto = self.__tela_quarto.pega_quarto_por_numero()
        
        for quarto in self.__quartos:
            if numero_do_quarto == quarto.numero_do_quarto:
                quarto_completo = {
                    'numero_do_quarto': quarto.numero_do_quarto,
                    'valor_diaria': quarto.valor_diaria,
                    'mobilias': quarto.mobilias,
                    'dias_reservados': quarto.dias_reservados
                }
                self.__tela_quarto.mostra_quartos(quarto_completo)
                return quarto
        self.__tela_quarto.sem_quartos_cadastrados()

    def lista_quartos(self):
        if not self.__quartos:
            self.__tela_quarto.sem_quartos_cadastrados()
            return None

        for quarto in self.__quartos:
            dados_quarto = {
                'numero_do_quarto': quarto.numero_do_quarto,
                'valor_diaria': quarto.valor_diaria,
                'dias_reservados': quarto.dias_reservados,
                'mobilias': quarto.mobilias,
            }
            self.__tela_quarto.mostra_quartos(dados_quarto)

    def adiciona_reserva(self, quarto, intervalo_reservado):
        for quarto in self.__quartos:
            if quarto in self.__quartos:
                quarto.adiciona_reserva(intervalo_reservado)

    def retornar(self):
        self.__controller_principal.abre_tela()

    def retorna_quartos(self):
        return self.__quartos

    def mostra_quartos(self, quarto):
        quarto_completo = {
            'numero_do_quarto':quarto.numero_do_quarto,
            'valor_diaria':quarto.valor_diaria,
            'mobilias':quarto.mobilias,
            'dias_reservados': quarto.dias_reservados
        }
        self.__tela_quarto.mostra_quartos(quarto_completo)
        

    def abre_tela(self):
        
        lista_opcoes = {
            1: self.inclui_quarto,
            2: self.excluir_quarto,
            3: self.busca_quarto_por_numero,
            4: self.lista_quartos,
            0: self.retornar
        }
        try:
            while True:
                lista_opcoes[self.__tela_quarto.abre_tela()]()

        except Exception:
            self.__tela_quarto.opcao_invalida()
            self.abre_tela()


