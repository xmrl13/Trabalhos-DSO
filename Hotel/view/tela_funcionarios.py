import PySimpleGUI as sg

class TelaFuncionarios():

    def abre_tela(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- Funcionario ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir funcionario', "RD1", key='1')],
            [sg.Radio('Alterar funcionario', "RD1", key='2')],
            [sg.Radio('Excluir funcionario', "RD1", key='3')],
            [sg.Radio('Busca funcionario', "RD1", key='4')],
            [sg.Radio('Listar funcionarios', "RD1", key='5')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('salvar'), sg.Cancel('Cancelar')]
        ]
        windows = sg.Window('Sistema de Funcionarios').Layout(layout)
        button,values = windows.Read()
        windows.close()
        return button, values

    def pega_funcionario_por_cracha(self):
        layout = [
            [sg.Text('Dados Funcionario')],
            [sg.Text('Cracha', size=(15, 1)), sg.InputText(key='cracha')],
            [sg.Submit('salvar'), sg.Cancel()]
        ]
        windows = sg.Window('Cadastro de Funcionario').Layout(layout)
        button, values = windows.Read()
        windows.close()
        return button, values



    def pega_dados_funcionario(self):
        layout = [
            [sg.Text('Dados Funcionario')],
            [sg.Text('Nome', size=(18, 1)), sg.InputText(key='nome_funcionario')],
            [sg.Text('Data de Nascimento', size=(18, 1)), sg.InputText(key='data_nascimento_funcionario')],
            [sg.Text('Cracha', size=(18, 1)), sg.InputText(key='cracha_do_funcionario')],
            [sg.Submit('salvar'), sg.Cancel()]
        ]
        windows = sg.Window('Cadastro de Funcionario').Layout(layout)
        button, values = windows.Read()
        windows.close()
        return button, values


    def altera_funcionario(self, funcionario):
        layout = [
            [sg.Text('Dados Funcionario')],
            [sg.Text('Nome', size=(15, 1)), sg.InputText(funcionario.nome, key='nome_funcionario')],
            [sg.Text('Data de Nascimento', size=(15, 1)), sg.InputText(funcionario.data_nascimento, key='data_nascimento_funcionario')],
            [sg.Text('Cracha', size=(15, 1)), sg.InputText(funcionario.cracha, key='cracha_do_funcionario')],
            [sg.Submit('salvar'), sg.Cancel()]
        ]
        windows = sg.Window('Cadastro de Funcionario').Layout(layout)
        button, values = windows.Read()
        windows.close()
        return button, values


    def mostra_funcionario(self, funcionario):
        string = (f'{funcionario.nome} \n {funcionario.data_nascimento} \n {funcionario.cracha}' )
        sg.Popup('_____________ Funcionario ____________', string)

    def reclama_funcionario(self):
        sg.Popup('_____________ Funcionario ____________', 'FUNCIONARIO NAO ENCONTRADO')
    
    def confirma_funcionario(self):
        sg.Popup('_____________ Funcionario ____________', 'ALTERAÇAO FEITA COM SUCESSO')
    
    def opcao_invalida(self):
        sg.Popup('_____________ Funcionario ____________', 'POR FAVOR DIGITE UM VALOR NÚMERICO E DENTRO DO INTERVALO VÁLIDO!')
    
    def funcionario_exitente(self):
        sg.Popup('_____________ Funcionario ____________', 'Funcionario com mesmo numero de cracha já existente')

    def sem_funcionarios_cadastrados(self):
        sg.Popup('_____________ Funcionario ____________', 'Sem funcionarios cadastrados!')
        