
class TelaAndar:

    def abre_tela(self):
        print(20 * '*')
        print("ANDAR")
        print(20 * '*')
        print(" Escolha a opçao ")
        print("1 - Incluir Andar")
        print("2 - Excluir Andar")
        print("3 - Lista Andares")
        print("0 - Retornar")
        opcao = int(input("Escolha a opcao: "))
        return opcao

    def inclui_andar(self):
        print('Cadastrar Andar')
        numero_andar = input('Numero do andar: ')
        return numero_andar

    def buscar_andar(self):
        print(20 * '*')
        andar = input("Insira o numero do andar que deseja: ")
        print(20 * '*')
        return andar

    def sem_andar_cadastrado(self):
        print('Sem nenhum andar cadastrados!')

    def mostra_andar(self, andar):
        print(20 * '*')
        print(f"Andar:{andar}º")

    def mostra_quarto_do_andar(self, quarto):
        print(f"- Quarto:{quarto}º")

    def reclama_quartos(self):
        print(20 * '*')
        print('SEM QUARTOS CADASTRADOS PARA ADICIONAR AO ANDAR')
        print(20 * '*')

    def mais_quartos(self):
        print(20 * '*')
        resposta = input('Deseja Adicionar Mais Um Quarto ? [S/N] ').upper()
        return resposta
        print(20 * '*')

    def reclama_andar(self):
        print(20 * '*')
        print('ANDAR NÃO EXISTENTE')
        print(20 * '*')
