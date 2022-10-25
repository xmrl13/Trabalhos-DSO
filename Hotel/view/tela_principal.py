
class TelaPrincipal:
    def abre_tela(self):
        print("-------- SISTEMA HOTEL ---------")
        print("Escolha sua opcao")
        print("1 - Funcionarios")
        print("2 - Clientes")
        print('3 - Reserva')
        print("0 - Encerrar")

        opcao = int(input("Escolha uma opção: "))
        return opcao
