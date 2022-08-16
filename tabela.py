import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

qtd_meses = int(input("Digite a quantidade de meses: "))
taxa_juros = float(input("Digite a taxa de juros mensal em %: ").replace(",", ".").replace("%","")) / 100
tipo_financiamento = input("Digite o tipo de financiamento SAC/PRICE: ").upper()
valor_financiado = float(input("Digite o valor a ser financiado: ").replace(",", "."))
print()
print("==============================================================")
print("||PARCELA | VLR.JUROS| AMORTIZAÇÃO |PRESTAÇÃO | SD. DEVEDOR ||")
print("==============================================================")


class Financiamento:

    def sistema_price(self):

        prestacao_price = valor_financiado * (
                    (((1 + taxa_juros) ** qtd_meses) * taxa_juros) / (((1 + taxa_juros) ** qtd_meses) - 1))
        saldo_devedor_price = valor_financiado
        i = 0
        total_juros_price = 0
        while i < qtd_meses:
            juros_price = saldo_devedor_price * taxa_juros
            amortizacao_price = prestacao_price - juros_price
            saldo_devedor_price = round(saldo_devedor_price - amortizacao_price, 6)
            total_juros_price +=juros_price
            i += 1
            print(
                f'|| {str(i).center(6)} | {str(locale.currency(juros_price,grouping=True, symbol=None).center(8))} | '
                f'{str(locale.currency(amortizacao_price,grouping=True, symbol=None).center(11))} |'
                f' {str(locale.currency(prestacao_price,grouping=True, symbol=None).center(8))} | '
                f'{str(locale.currency(saldo_devedor_price,grouping=True, symbol=None).center(11))} ||')
        print("==============================================================")
        print(f'O valor total de Juros a ser pago é de: R$ {locale.currency(total_juros_price,grouping=True, symbol=None)}')
        print(f'O valor total a ser pago no financiamento é de: R$ {locale.currency((prestacao_price*qtd_meses),grouping=True, symbol=None)}')
        print("==============================================================")

    def sistema_sac(self):
        parcela_fixa_sac = valor_financiado / qtd_meses
        saldo_devedor_sac = valor_financiado
        total_juros_sac = 0
        total_prestacao_sac = 0
        i = 0
        while i < qtd_meses:
            juros_sac = saldo_devedor_sac * taxa_juros
            prestacao_sac = juros_sac + parcela_fixa_sac
            saldo_devedor_sac = saldo_devedor_sac - parcela_fixa_sac
            total_juros_sac+=juros_sac
            total_prestacao_sac += prestacao_sac
            i += 1
            print(
                f'|| {str(i).center(6)} | {str(locale.currency(juros_sac,grouping=True, symbol=None).center(8))} |'
                f' {str(locale.currency(parcela_fixa_sac,grouping=True, symbol=None).center(11))} |'
                f' {str(locale.currency(prestacao_sac,grouping=True, symbol=None).center(8))} |'
                f' {str(locale.currency(saldo_devedor_sac,grouping=True, symbol=None).center(11))} ||')
        print("==============================================================")
        print(f'O valor total de Juros a ser pago é de: R$ {locale.currency(total_juros_sac,grouping=True, symbol=None)}')
        print(f'O valor total a ser pago no financiamento é de: R$ {locale.currency(total_prestacao_sac,grouping=True, symbol=None)}')
        print("==============================================================")

    def calcula(self):
        if (tipo_financiamento == "PRICE"):
            Financiamento.sistema_price(tipo_financiamento)
        elif (tipo_financiamento == "SAC"):
            Financiamento.sistema_sac(tipo_financiamento)
        else:
            print("digite um sistema de financiamento válido")


Financiamento.calcula(Financiamento)