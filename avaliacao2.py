preco = int(input(' Digite o valor do preço do produto: '))
valor_pago = int(input(' Digite o valor pago pelo cliente: '))

cedula = [100,50,20,10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]


def calcular_troco (x,y):
    if(valor_pago < preco):
        print('\n O valor pago pelo cliente não é suficiente para a compra do produto.')
    elif(valor_pago == preco):
        print('\n Troco ao cliente é de R$ 0,00.')
    else:
        troco = valor_pago - preco
    
