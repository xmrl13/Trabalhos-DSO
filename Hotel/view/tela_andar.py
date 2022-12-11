import PySimpleGUI as sg
class TelaAndar:

    def abre_tela(self):
        print(20 * '*')
        print("ANDAR")
        print(20 * '*')
        print(" Escolha a opçao ")
        print("1 - Incluir Andar")
        print("2 - Adicionar quarto ao andar")
        print("3 - Excluir Andar")
        print("4 - Lista Andares")
        print("0 - Retornar")
        opcao = int(input("Escolha a opcao: "))
        return opcao

    def inclui_andar(self):
        print('Cadastrar Andar')
        numero_andar = input('Numero do andar: ')
        verifica_numero_andar = numero_andar.isnumeric()
        if not verifica_numero_andar:
            print('DIGITE APENAS NÚMEROS PARA O NÚMERO DO ANDAR!')
            return None
        numero_andar = int(numero_andar)
        return numero_andar

    def buscar_andar(self):
        print(20 * '*')
        andar = int(input("Insira o numero do andar que deseja: "))
        print(20 * '*')
        return andar

    def sem_andar_cadastrado(self):
        print('Sem nenhum andar cadastrados!')

    def mostra_andar(self, andar):
        string = (f'Número do andar: {andar.numero}°')
        sg.Popup('-------Andares cadastrados no Sistema-------', string)
   

    def reclama_quartos(self):
        print(20 * '*')
        print('SEM QUARTOS CADASTRADOS PARA ADICIONAR AO ANDAR')
        print(20 * '*')

    def mais_quartos(self):
        print(20 * '*')
        resposta = input('Deseja Adicionar Mais Um Quarto ? [S/N] ').upper()
        print(20 * '*')
        return resposta


    def reclama_andar(self):
        print(20 * '*')
        print('ANDAR NÃO EXISTENTE')
        print(20 * '*')
    
    def reclama_andar_sem_quarto(self):
        print(20 * '*')
        print('ANDAR SEM QUARTOS CADASTRADOS')
        print(20 * '*')

    def andar_excluido(self):
        print(20 * '*')
        print('ANDAR EXCLUIDO')
        print(20 * '*')


    def opcao_invalida(self):
        print(20 * '*')
        print('POR FAVOR DIGITE UM VALOR NÚMERICO E DENTRO DO INTERVALO VÁLIDO!')
        print(20 * '*')