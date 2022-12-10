import PySimpleGUI as sg

class TelaFuncionarios():
    def abre_tela(self):
        print(20 * '*')
        print("FUNCIONARIOS")
        print(20 * '*')
        print(" Escolha a opçao ")
        print("1 - Incluir funcionario")
        print("2 - Alterar funcionario")
        print("3 - Excluir funcionario")
        print("4 - Busca funcionario")
        print("5 - Listar funcionarios")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))

        return opcao

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
        pass

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
        