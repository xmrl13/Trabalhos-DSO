import PySimpleGUI as sg

class TelaReserva():
    
    def abre_tela(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- Reserva ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Cadastrar reserva', "RD1", key='1')],
            [sg.Radio('Remover Reserva', "RD1", key='2')],
            [sg.Radio('Voltar', "RD1", key='0')],
            [sg.Button('salvar'), sg.Cancel('Cancelar')]
        ]
        windows = sg.Window('Sistema de Reserva').Layout(layout)
        button,values = windows.Read()
        windows.close()
        return button, values

    

    def pega_data_da_reserva(self):

        layout = [
            [sg.Text('Dados Reserva')],
            [sg.Text('Dia de entrada', size=(18, 1)), sg.InputText(key='dia_entrada')],
            [sg.Text('Mes de entrada', size=(18, 1)), sg.InputText(key='mes_entrada')],
            [sg.Text('Ano de entrada', size=(18, 1)), sg.InputText(key='ano_entrada')],

            [sg.Text('Dia de saida', size=(18, 1)), sg.InputText(key='dia_saida')],
            [sg.Text('Mes de saida', size=(18, 1)), sg.InputText(key='mes_saida')],
            [sg.Text('Ano de saida', size=(18, 1)), sg.InputText(key='ano_saida')],
            [sg.Submit('salvar'), sg.Cancel()]
        ]
        windows = sg.Window('Cadastro de Funcionario').Layout(layout)
        button, values = windows.Read()
        windows.close()
        return button, values


    def reclama_reserva(self):
        sg.Popup('             Reserva             ', 'Intervalo já Reservado')
        
    
    def confirma_reserva(self):
        sg.Popup('             Reserva             ', 'Reserva efetuada com sucesso')
        
    
    def reserva_excluida(self):
        sg.Popup('             Reserva             ', 'Reserva excluida com sucesso!')
    
    def data_errada(self):
        sg.Popup('             Reserva             ', 'Data inexistente inserida')
    
    def opcao_invalida(self):
        print(20 * '*')
        print('POR FAVOR DIGITE UM VALOR NÚMERICO E DENTRO DO INTERVALO VÁLIDO!')
        print(20 * '*')
