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
        self.__controller_principal.controller_clientes.lista_clientes()
        cliente = self.__controller_principal.controller_clientes.busca_cliente_por_cpf()



    def altera_reserva(self):
        pass

    def excluir_reserva(self):
        pass

    def busca_reserva(self):
        pass
    
    def abre_tela(self):
        pass

'''
from controller_principal import ControllerPrincipal

controle_principal = ControllerPrincipal()

controle_reserva = ControllerReserva(controle_principal)
'''
#