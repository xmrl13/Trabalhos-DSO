from controller_funcionarios import ControllerFuncionarios
from controller_tipo_quarto import ControllerTipoQuarto
from controller_quarto import ControllerQuarto
from controller_reserva import ControllerReserva
from controller_clientes import ControllerClientes
from controller_andar import ControllerAndar


class ControllerPrincipal:
    def __init__(self):
        self.__controller_funcionarios = ControllerFuncionarios(self)
        self.__controller_tipo_quarto = ControllerTipoQuarto(self)
        self.__controller_quarto = ControllerQuarto(self)
        self.__controller_reserva = ControllerReserva(self)
        self.__controller_clientes = ControllerClientes(self)
        self.__controller_andar = ControllerAndar(self)
    
    def cadastra_funcionario(self):
        self.__controller_funcionarios.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def inicializa_sistema(self):
        self.abre_tela()
    
    
    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_funcionario}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
