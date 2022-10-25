

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