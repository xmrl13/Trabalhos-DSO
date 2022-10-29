
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

        opcao = input("Escolha uma opção: ")
        while True:
            if opcao == '1' or opcao == '2' or opcao == '3' or opcao == '4' or opcao == '5' or opcao == '0':
                break
            
            self.opcao_invalida()
            opcao = input("Escolha uma opção: ")

        opcao = int(opcao)
        return opcao

    def opcao_invalida(self):
        print(20 * '*')
        print('POR FAVOR DIGITE UM VALOR NÚMERICO E DENTRO DO INTERVALO VÁLIDO!')
        print(20 * '*')
    
    def sistema_encerrado(self):
        print(5 * '-', 'Sistema encerrado', 5 * '-')