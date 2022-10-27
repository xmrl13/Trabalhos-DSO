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
            reservas.append(intervalo_reservado)
            print(self.__reservas)
            return
        
        for reservas_efetuadas in reservas:
            if intervalo_reservado.is_intersection(reservas_efetuadas):
                print('Intervalo já reservado')
            else:
                print('Intervalo não reservado reservado')
        

    def altera_reserva(self):
        ...

    def excluir_reserva(self):
        ...

    def busca_reserva(self):
        ...

    def lista_reserva(self):
        ...
    
    def retornar(self):
        self.__controller_principal.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.inclui_reserva, 2: self.altera_reserva, 3: self.excluir_reserva,
         4: self.busca_reserva, 5: self.lista_reserva, 0: self.retornar}


        while True:
            opcao = self.__tela_reserva.abre_tela()
            lista_opcoes[opcao]()
