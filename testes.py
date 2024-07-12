preco = float(input('Digite o valor do preço do produto: '))
valor_pago = float(input('Digite o valor pago pelo cliente: '))


def calcular_troco(preco, valor_pago):
    if valor_pago < preco:
        print('\nO valor pago pelo cliente não é suficiente para a compra do produto.')
    elif valor_pago == preco:
        print('\nTroco ao cliente é de R$ 0,00.')
    else:
        troco = valor_pago - preco
        print('\nTroco ao cliente é de R$ {:.2f}.'.format(troco))
        print('-----------------------------------------')
        print('Desglose do troco:')
        # Agora vamos calcular as cédulas e moedas a serem devolvidas
        for cedula_valor in cedula:
            quantidade = troco // cedula_valor
            if quantidade > 0:
                if cedula_valor >= 1:
                    print(f'{int(quantidade)} nota(s) de R$ {cedula_valor:.2f}')
                else:
                    print(f'{int(quantidade)} moeda(s) de R$ {cedula_valor:.2f}')
                troco -= quantidade * cedula_valor
            if troco == 0:
                break

calcular_troco(preco, valor_pago)
