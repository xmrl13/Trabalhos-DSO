from view.tela_principal import TelaPrincipal
from controller.controller_funcionarios import ControllerFuncionarios
from controller.controller_quarto import ControllerQuarto
from controller.controller_reserva import ControllerReserva
from controller.controller_clientes import ControllerClientes
from controller.controller_andar import ControllerAndar


class ControllerPrincipal:
    def __init__(self):
        self.__controller_funcionarios = ControllerFuncionarios(self)
        self.__controller_quarto = ControllerQuarto(self)
        self.__controller_reserva = ControllerReserva(self)
        self.__controller_clientes = ControllerClientes(self)
        self.__controller_andar = ControllerAndar(self)
        self.__tela_principal = TelaPrincipal()

    @property
    def controller_funcionarios(self):
        return self.__controller_funcionarios

    @property
    def controller_quarto(self):
        return self.__controller_quarto

    @property
    def controller_reserva(self):
        return self.__controller_reserva

    @property
    def controller_clientes(self):
        return self.__controller_clientes
    
    @property
    def controller_andar(self):
        return self.__controller_andar

    def retorna_quartos(self):
        return self.__controller_quarto.retorna_quartos()
    
    def pega_quartos(self):
        return self.controller_quarto.busca_quarto_por_numero()

    def mostra_quarto(self, quarto):
        return self.controller_quarto.mostra_quarto(quarto)


    def inicializa_funcionario(self):
        self.__controller_funcionarios.abre_tela()

    def inicializa_quarto(self):
        self.__controller_quarto.abre_tela()

    def inicializa_reserva(self):
        self.__controller_reserva.abre_tela()

    def inicializa_cliente(self):
        self.__controller_clientes.abre_tela()

    def inicializa_andar(self):
        self.__controller_andar.abre_tela()

    def inicializa_sistema(self):
        self.abre_tela()
    
    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {
            1: self.inicializa_funcionario,
            2: self.inicializa_cliente,
            3: self.inicializa_reserva,
            4: self.inicializa_quarto,
            5: self.inicializa_andar,
            0: self.encerra_sistema
                        }

        while True:
            opcao_escolhida = self.__tela_principal.abre_tela()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
            #
