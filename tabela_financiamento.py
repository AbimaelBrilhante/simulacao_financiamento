import locale

class Financiamento:

    def __init__(self):
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        self.qtd_meses = int(input("Digite a quantidade de meses: "))
        self.taxa_juros = float(input("Digite a taxa de juros mensal em %: ").replace(",", ".").replace("%", "")) / 100
        self.tipo_financiamento = input("Digite o tipo de financiamento SAC/PRICE: ").upper()
        self.valor_financiado = float(input("Digite o valor a ser financiado: ").replace(",", "."))
        print()
        print("==============================================================")
        print("||PARCELA | VLR.JUROS| AMORTIZAÇÃO |PRESTAÇÃO | SD. DEVEDOR ||")
        print("==============================================================")

        if (self.tipo_financiamento == "PRICE"):
           self.sistema_price()
        elif (self.tipo_financiamento == "SAC"):
            self.sistema_sac()
        else:
            print("digite um sistema de financiamento válido")


    def sistema_price(self):

        prestacao_price = self.valor_financiado * (
                (((1 + self.taxa_juros) ** self.qtd_meses) * self.taxa_juros) / (((1 + self.taxa_juros) ** self.qtd_meses) - 1))
        saldo_devedor_price = self.valor_financiado
        i = 0
        total_juros_price = 0
        while i < self.qtd_meses:
            juros_price = saldo_devedor_price * self.taxa_juros
            amortizacao_price = prestacao_price - juros_price
            saldo_devedor_price = round(saldo_devedor_price - amortizacao_price, 6)
            total_juros_price += juros_price
            i += 1
            print(
                f'|| {str(i).center(6)} | {str(locale.currency(juros_price, grouping=True, symbol=None).center(8))} | '
                f'{str(locale.currency(amortizacao_price, grouping=True, symbol=None).center(11))} |'
                f' {str(locale.currency(prestacao_price, grouping=True, symbol=None).center(8))} | '
                f'{str(locale.currency(saldo_devedor_price, grouping=True, symbol=None).center(11))} ||')
        print("==============================================================")
        print(
            f'O valor total de Juros a ser pago é de: R$ {locale.currency(total_juros_price, grouping=True, symbol=None)}')
        print(
            f'O valor total a ser pago no financiamento é de: R$ {locale.currency((prestacao_price * self.qtd_meses), grouping=True, symbol=None)}')
        print("==============================================================")

    def sistema_sac(self):
        parcela_fixa_sac = self.valor_financiado / self.qtd_meses
        saldo_devedor_sac = self.valor_financiado
        total_juros_sac = 0
        total_prestacao_sac = 0
        i = 0
        while i < self.qtd_meses:
            juros_sac = saldo_devedor_sac * self.taxa_juros
            prestacao_sac = juros_sac + parcela_fixa_sac
            saldo_devedor_sac = saldo_devedor_sac - parcela_fixa_sac
            total_juros_sac += juros_sac
            total_prestacao_sac += prestacao_sac
            i += 1
            print(
                f'|| {str(i).center(6)} | {str(locale.currency(juros_sac, grouping=True, symbol=None).center(8))} |'
                f' {str(locale.currency(parcela_fixa_sac, grouping=True, symbol=None).center(11))} |'
                f' {str(locale.currency(prestacao_sac, grouping=True, symbol=None).center(8))} |'
                f' {str(locale.currency(saldo_devedor_sac, grouping=True, symbol=None).center(11))} ||')
        print("==============================================================")
        print(
            f'O valor total de Juros a ser pago é de: R$ {locale.currency(total_juros_sac, grouping=True, symbol=None)}')
        print(
            f'O valor total a ser pago no financiamento é de: R$ {locale.currency(total_prestacao_sac, grouping=True, symbol=None)}')
        print("==============================================================")


if __name__ == "__main__":
    Financiamento()