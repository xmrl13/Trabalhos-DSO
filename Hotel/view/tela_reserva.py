

class TelaReserva():
    
    def abre_tela(self):
        print(5 * '*')
        print('Reserva')
        print(5 * '*')
        print('1 - Cadastrar Reserva')
        print('2 - Remover Reserva')
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

    def reclama_reserva(self):
        print('Intervalo já reservado.')
        return
    
    def confirma_reserva(self):
        print('Reserva efetuada com sucesso.')
        return
    
    def reserva_excluida(self):
        print('Reserva excluida com sucesso!')
    
    def data_errada(self):
        print(5 * '*')
        print('Data inexistente inserida.')
        print(5 * '*')
        return
    
    def opcao_invalida(self):
        print(20 * '*')
        print('POR FAVOR DIGITE UM VALOR NÚMERICO E DENTRO DO INTERVALO VÁLIDO!')
        print(20 * '*')
