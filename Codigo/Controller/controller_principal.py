from controller_andar import ControllerAndar
from controller_clientes import ControllerClientes
from controller_funcionarios import ControllerFuncionarios
from controller_quarto import ControllerQuarto
from controller_reserva import ControllerReserva
from controller_tipo_quarto import ControllerTipoQuarto

class ControllerPrincipal:
    def __init__(self):
        self.__controller_funcionarios = ControllerFuncionarios(self)
        self.__controller_tipo_quarto = ControllerTipoQuarto(self)
        self.__controller_quarto = ControllerQuarto(self)
        self.__controller_reserva = ControllerReserva(self)
        self.__controller_clientes = ControllerClientes(self)
        self.__controller_andar = ControllerAndar(self)