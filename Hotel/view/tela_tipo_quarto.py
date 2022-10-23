
class TelaTipoQuarto:

    def abre_tela(self):
        print(20 * '*')
        print("TipoQuarto")
        print(20 * '*')
        print(" Escolha a opçao ")
        print("1 - Incluir TipoQuarto")
        print("2 - Alterar TipoQuarto")
        print("3 - Excluir TipoQuarto")
        print("4 - Busca TipoQuarto")
        print("5 - Mostra TipoQuarto")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))

        return opcao

    def pega_dados_tipo_quarto(self):
        print('CADASTRO DO Tipo Quarto')
        tamanho_quarto = float(input('Tamanho Do Quarto [Metros Quadrados]: '))
        quantidade_camas = int(input('Quantidade De Camas: '))
        jacuzzi = input('Possui Jacuzzi? [S]/[N] ')
        while True:
            if jacuzzi.upper() == 'S':
                jacuzzi = True
                break
            elif jacuzzi.upper() == 'N':
                jacuzzi = False
                break
            else:
                print('Insira apenas S ou N em Jacuzzi ')
                jacuzzi = input('Possui Jacuzzi? [S]/[N] ')

        return {
            'tamanho_quarto': tamanho_quarto,
            'quantidade_camas': quantidade_camas,
            'jacuzzi': jacuzzi,
        }

    def reclama_tipo_quarto(self):
        print(20 * '*')
        print(f"Quarto Inesistente ")
        print(20 * '*')

    def mostra_tipo_quarto(self, tipo_quarto):
        print(20 * '*')
        print(f"Tamanho do Quarto (em m2) : {tipo_quarto['tamanho_quarto']}")
        print(
            f"Numero de Camas presente no Quarto : {tipo_quarto['quantidade_camas']}")
        print(f"Possui Jacuzzi: {tipo_quarto['jacuzzi']}")
        print(20 * '*')

    def pega_quarto_por_tamanho(self):
        tamanho = float(input(
            'Digite o tamanho do quarto desejado: '))
        return tamanho

    def confirma_tipo_quarto(self):
        print(20 * '*')
        print("ALTERAÇÃO FEITA COM SUCESSO")
        print(20 * '*')

    def altera_tipo_quarto(self):
        print('ALTERAR DADOS DO  TIPO DO QUARTO')
        tamanho_quarto = float(input('Tamanho Do Quarto [Metros Quadrados]: '))
        quantidade_camas = int(input('Quantidade De Camas: '))
        jacuzzi = input('Possui Jacuzzi? [S]/[N] ')
        while True:
            if jacuzzi.upper() == 'S':
                jacuzzi = True
                break
            elif jacuzzi.upper() == 'N':
                jacuzzi = False
                break
            else:
                print('Insira apenas S ou N em Jacuzzi ')
                jacuzzi = input('Possui Jacuzzi? [S]/[N] ')

        return {
            'tamanho_quarto': tamanho_quarto,
            'quantidade_camas': quantidade_camas,
            'jacuzzi': jacuzzi,
        }
