
class TelaQuarto:

    def abre_tela(self):
        print(20 * '*')
        print("QUARTOS")
        print(20 * '*')
        print(" Escolha a opçao ")
        print("1 - Incluir Quarto")
        print("2 - Alterar Quarto")
        print("3 - Excluir Quarto")
        print("4 - Busca Quarto")
        print("5 - Mostra Quarto")
        print("0 - Retornar")
        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_quarto(self):
        print('CADASTRO DO QUARTO')
        numero_do_quarto = input('Numero do quarto: ')
        valor_da_diaria = input('Valor da diaria: ')
        mobilias = []
        while True:
            rest = input('deseja incluir mobilia? [S/N]').upper()
            if rest == 'N':
                break
            descricao = input("Descrição da mobilia: ")
            quantidade = int(input("Quantidade: "))
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

    def quarto_excluido(self):
        print(20 * '*')
        print('Quarto excluido com sucessso')
        print(20 * '*')

    def mostra_quartos(self, dados_quarto):
        print(20 * '*')
        print(f"Número do quarto: {dados_quarto['numero_do_quarto']}")
        print(f"Valor da diária: {dados_quarto['valor_diaria']}")
        print(5 * '*', 'Reservas', 5 * '*')
        if not dados_quarto['dias_reservados']:
            print('Sem reservas cadastradas para esse quarto')
        else:
            print(f"Dias Reservados: {dados_quarto['dias_reservados']}")
        print(5 * '*', 'Mobilias', 5 * '*')
        for dados_mobilia in dados_quarto['mobilias']:
            print(f"Mobila: {dados_mobilia.descricao},Quantidade: {dados_mobilia.quantidade}")

    def pega_novos_dados_quarto(self):
        print('CADASTRO NOVO QUARTO')
        numero_do_quarto = input('Numero do quarto: ')
        valor_da_diaria = input('Valor da diaria: ')
        mobilias = []
        while True:
            rest = input('deseja incluir mobilia? [S/N]').upper()
            if rest == 'N':
                break
            descricao = input("Descrição da mobilia: ")
            quantidade = int(input("Quantidade: "))
            mobilias.append({'descricao': descricao, 'quantidade': quantidade})
        return {
            'numero_do_quarto': numero_do_quarto,
            'valor_da_diaria': valor_da_diaria,
            'mobilias': mobilias,
        }

    def opcao_invalida(self):
        print(20 * '*')
        print('POR FAVOR DIGITE UM VALOR NÚMERICO E DENTRO DO INTERVALO VÁLIDO!')
        print(20 * '*')


