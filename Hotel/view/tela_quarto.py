import PySimpleGUI as sg
class TelaQuarto:

    def abre_tela(self):
        print(20 * '*')
        print("QUARTOS")
        print(20 * '*')
        print(" Escolha a opçao ")
        print("1 - Incluir Quarto")
        print("2 - Excluir Quarto")
        print("3 - Busca Quarto")
        print("4 - Listar Quartos")
        print("0 - Retornar")
        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_quarto(self):
        print('CADASTRO DO QUARTO')
        numero_do_quarto = input('Numero do quarto: ')
        verifica_numero_do_quarto = numero_do_quarto.isnumeric()
        if not verifica_numero_do_quarto:
            print('DIGITE APENAS NÚMEROS PARA O NÚMERO DO QUARTO!')
            return None

        valor_da_diaria = input('Valor da diaria: ')
        verifica_valor_da_diaria = valor_da_diaria.isnumeric()
        if not verifica_valor_da_diaria:
            print('DIGITE APENAS NÚMEROS PARA O VALOR DA DIÁRIA!')
            return None
        valor_da_diaria = float(valor_da_diaria)

        mobilias = []
        while True:
            rest = input('deseja incluir mobilia? [S/N]').upper()
            if rest == 'N':
                break
            descricao = input("Descrição da mobilia: ")
            valida_descricao = descricao.isalpha()
            if not valida_descricao:
                print('DIGITE APENAS LETRAS PARA A DESCRIÇÃO DA MOBILIA!')
                return None
            
            quantidade = input("Quantidade: ")
            valida_quantidade = quantidade.isnumeric()
            if not valida_quantidade:
                print('DIGITE APENAS NÚMEROS PARA A QUANTIDE DE MOBILIA!')
                return None
            quantidade = int(quantidade)
            mobilias.append({'descricao': descricao, 'quantidade': quantidade})
        return {
            'numero_do_quarto': numero_do_quarto,
            'valor_da_diaria': valor_da_diaria,
            'mobilias': mobilias
        }

    def pega_quarto_por_numero(self):
        numero_do_quarto = input(
            'Digite o numero do quarto que deseja localizar: ')
        return numero_do_quarto

    def sem_quartos_cadastrados(self):
        print('Sem quarto(s) cadastrado(s)!')

    def quarto_com_reserva(self):
        string = (f'Este quarto contem uma ou mais reservas, para excluir o quarto primeiro exclua as reservas!')
        sg.Popup('----Quarto com reservas efetuadas!----', string)

    def quarto_excluido(self):
        string = (f'Quarto excluido com sucesso!')
        sg.Popup('---Quarto excluido---', string)

    def mostra_quartos(self, quarto, dados_quarto):
        string = (f'Número do quarto: {quarto.numero_do_quarto} \nValor da diária: {quarto.valor_diaria}R$ \nDias reservados: {quarto.dias_reservados}')
        sg.Popup('-------Quartos cadastrados no Sistema-------', string)
        for dados in dados_quarto['mobilias']:
            string2 = (f'Mobilias do quarto n°{quarto.numero_do_quarto} \nDescrição da mobilia: {dados.descricao} \nQuantidade: {dados.quantidade}')
            sg.Popup('--------Mobilias--------', string2)
   
    def opcao_invalida(self):
        print(20 * '*')
        print('POR FAVOR DIGITE UM VALOR NUMERICO E DENTRO DO INTERVALO VÁLIDO!')
        print(20 * '*')


