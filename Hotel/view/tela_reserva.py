

class TelaReserva():
    
    def abre_tela(self):
        print(5 * '*')
        print('Reserva')
        print(5 * '*')
        print('1 - Cadastrar Reserva')
        print('2 - Alterar Reserva')
        print('3 - Remover Reserva')
        print('4 - Buscar Reserva')
        print('5 - Listar Reserva')
        print('0 - Voltar')
        opcao = int(input('Digite uma opção: '))
        return opcao

    def pega_data_da_reserva(self):
        print(5 * '*')
        dia_entrada = int(input('Digite o dia que deseja reservar (DD): '))
        mes_entrada = int(input('Digite o mês que deseja reservar (MM): '))
        ano_entrada = int(input('Digite o ano que deseja reservar (AAAA): '))
        print(5 * '*')
        dia_saida = int(input('Digite o dia que deseja encerrar a reserva (DD): '))
        mes_saida = int(input('Digite o mês que deseja encerrar a reserva (MM): '))
        ano_saida = int(input('Digite o ano que deseja encerrar a reserva (AAAA): '))
        print(5 * '*')
        return {
            'dia_entrada': dia_entrada,
            'mes_entrada': mes_entrada,
            'ano_entrada': ano_entrada,
            'dia_saida': dia_saida,
            'mes_saida': mes_saida,
            'ano_saida': ano_saida
        }