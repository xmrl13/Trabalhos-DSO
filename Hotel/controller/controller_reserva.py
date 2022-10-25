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
        self.__controller_principal.controller_clientes.lista_cliente()

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

'''
from controller_principal import ControllerPrincipal

controle_principal = ControllerPrincipal()

controle_reserva = ControllerReserva(controle_principal)
'''
#