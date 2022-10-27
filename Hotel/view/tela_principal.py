
class TelaPrincipal:
    def abre_tela(self):
        print("-------- SISTEMA HOTEL ---------")
        print("Escolha uma opção")
        print("1 - Funcionarios")
        print("2 - Clientes")
        print('3 - Reservas')
        print('4 - Quartos')
        print('5 - Andares')
        print("0 - Encerrar")

        opcao = int(input("Escolha uma opção: "))
        return opcao
