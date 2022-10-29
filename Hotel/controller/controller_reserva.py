import datetime
import datetimerange
from view.tela_reserva import TelaReserva
from model.reserva import Reserva
class ControllerReserva:
    def __init__(self, controller_principal):
        self.__controller_principal = controller_principal
        self.__tela_reserva = TelaReserva()
        self.__reservas = []

    def inclui_reserva(self):
        cliente = self.__controller_principal.controller_clientes.busca_cliente_por_cpf()
        quarto = self.__controller_principal.controller_quarto.busca_quarto_por_numero()
        reservas = self.__controller_principal.controller_quarto.retorna_reservas(quarto)
        data_da_reserva = self.__tela_reserva.pega_data_da_reserva()
        entrada_reserva = datetime.datetime(
            data_da_reserva['ano_entrada'],
            data_da_reserva['mes_entrada'],
            data_da_reserva['dia_entrada'])
            
        saida_reserva = datetime.datetime(
            data_da_reserva['ano_saida'],
            data_da_reserva['mes_saida'],
            data_da_reserva['dia_saida'])
        intervalo_reservado = datetimerange.DateTimeRange(entrada_reserva, saida_reserva)

        if not reservas:
            self.__reservas.append(Reserva(quarto, cliente, intervalo_reservado))
            self.__controller_principal.controller_quarto.adiciona_reserva(quarto, intervalo_reservado)
            self.__tela_reserva.confirma_reserva()
            return
        
        for reservas_efetuadas in reservas:
            if intervalo_reservado.is_intersection(reservas_efetuadas):
                self.__tela_reserva.reclama_reserva()
                return
            else:
                self.__reservas.append(Reserva(quarto, cliente, intervalo_reservado))
                self.__controller_principal.controller_quarto.adiciona_reserva(quarto, intervalo_reservado)
                self.__tela_reserva.confirma_reserva()
        

    def excluir_reserva(self):
        data_reservada = self.__tela_reserva.pega_data_da_reserva()
        entrada_reserva = datetime.datetime(
            data_reservada['ano_entrada'],
            data_reservada['mes_entrada'],
            data_reservada['dia_entrada'])
            
        saida_reserva = datetime.datetime(
            data_reservada['ano_saida'],
            data_reservada['mes_saida'],
            data_reservada['dia_saida'])
        intervalo_reservado = datetimerange.DateTimeRange(entrada_reserva, saida_reserva)
        if intervalo_reservado in self.__reservas:
            self.__reservas.pop(intervalo_reservado)
            print('Apaguei')
            print(self.__reservas)
    
    def retornar(self):
        self.__controller_principal.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.inclui_reserva, 2: self.excluir_reserva, 0: self.retornar}


        while True:
            opcao = self.__tela_reserva.abre_tela()
            lista_opcoes[opcao]()
