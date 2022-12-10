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
        windows = sg.Window('Sistema de livros').Layout(layout)
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
        print(20 * '*')
        print(funcionario.nome)
        print(funcionario.data_nascimento)
        print(funcionario.cracha)
        print(20 * '*')

    def reclama_funcionario(self):
        print(20 * '*')
        print('FUNCIONARIO NAO ENCONTRADO')
        print(20 * '*')
    
    def confirma_funcionario(self):
        print(20 * '*')
        print('ALTERAÇAO FEITA COM SUCESSO')
        print(20 * '*')
    
    def opcao_invalida(self):
        print(20 * '*')
        print('POR FAVOR DIGITE UM VALOR NÚMERICO E DENTRO DO INTERVALO VÁLIDO!')
        print(20 * '*')
    
    def funcionario_exitente(self):
        print(20 * '*')
        print('Funcionario com mesmo numero de cracha já existente')
        print(20 * '*')

    def sem_funcionarios_cadastrados(self):
        print('Sem funcionarios cadastrados!')
        