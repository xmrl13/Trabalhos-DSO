import datetime
import datetimerange
from view.tela_reserva import TelaReserva
from model.reserva import Reserva
from model.quarto import Quarto


class ControllerReserva:
    def __init__(self, controller_principal):
        self.__controller_principal = controller_principal
        self.__tela_reserva = TelaReserva()

    def inclui_reserva(self):
        #try:
            cliente = self.__controller_principal.controller_clientes.busca_cliente_por_cpf()
            if cliente is None:
                return
            quarto = self.__controller_principal.controller_quarto.busca_quarto_por_numero()
            if quarto is None:
                return
            funcionario = self.__controller_principal.controller_funcionarios.busca_funcionario()
            if funcionario is None:
                return
            reservas = self.__controller_principal.controller_quarto.retorna_reservas(quarto)

            resposta, data_da_reserva = self.__tela_reserva.pega_data_da_reserva()

            if resposta != 'salvar':
                return

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
                self.__controller_principal.controller_quarto.adiciona_reserva(quarto, intervalo_reservado)
                self.__tela_reserva.confirma_reserva()
                return
            
            for reservas_efetuadas in reservas:
                if intervalo_reservado.is_intersection(reservas_efetuadas):
                    self.__tela_reserva.reclama_reserva()
                    return
                else:
                    self.__controller_principal.controller_quarto.adiciona_reserva(quarto, intervalo_reservado)
                    self.__tela_reserva.confirma_reserva()
        '''except:
            self.__tela_reserva.data_errada()
            self.abre_tela()'''
            

    def excluir_reserva(self):
        #try:
        quarto = self.__controller_principal.controller_quarto.busca_quarto_por_numero()
        dias_reservados = self.__controller_principal.controller_quarto.retorna_reservas(quarto)
        data_para_conferir = self.__tela_reserva.pega_data_da_reserva()
        entrada_para_conferir = datetime.datetime(
        data_para_conferir['ano_entrada'],
        data_para_conferir['mes_entrada'],
        data_para_conferir['dia_entrada'])

        saida_para_conferir = datetime.datetime(
        data_para_conferir['ano_saida'],
        data_para_conferir['mes_saida'],
        data_para_conferir['dia_saida'])

        intervalo_para_conferir = datetimerange.DateTimeRange(entrada_para_conferir, saida_para_conferir)

        for reservas_efetuadas in dias_reservados:
            if intervalo_para_conferir.is_intersection(reservas_efetuadas):
                dias_reservados.remove(intervalo_para_conferir)
                self.__tela_reserva.reserva_excluida()
                return
        '''except:
            self.__tela_reserva()
            self.abre_tela()'''

    def retornar(self):
        self.__controller_principal.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.inclui_reserva, 2: self.excluir_reserva, 0: self.retornar}

        while True:
            resposta, dados = self.__tela_reserva.abre_tela()
            print(dados)
            if resposta != 'salvar':
                self.retornar()

            if dados['1']:
                lista_opcoes[1]()

            if dados['2']:
                lista_opcoes[2]()

            if dados['0']:
                lista_opcoes[0]()

