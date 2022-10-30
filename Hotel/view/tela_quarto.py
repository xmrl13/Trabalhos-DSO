
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

    def quarto_excluido(self):
        print(20 * '*')
        print('Quarto excluido com sucessso')
        print(20 * '*')

    def mostra_quartos(self, dados_quarto):
        print(20 * '*')
        print(f"Número do quarto: {dados_quarto['numero_do_quarto']}")
        print(f"Valor da diária: {dados_quarto['valor_diaria']:.2f}'R$'")
        print(5 * '*', 'Reservas', 5 * '*')
        if not dados_quarto['dias_reservados']:
            print('Sem reservas cadastradas para esse quarto')
        else:
            print(f"Dias Reservados: {dados_quarto['dias_reservados']}")
        print(5 * '*', 'Mobilias', 5 * '*')
        for dados_mobilia in dados_quarto['mobilias']:
            print(f"Mobila: {dados_mobilia.descricao}, quantidade: {dados_mobilia.quantidade}")

    def opcao_invalida(self):
        print(20 * '*')
        print('POR FAVOR DIGITE UM VALOR NUMERICO E DENTRO DO INTERVALO VÁLIDO!')
        print(20 * '*')


