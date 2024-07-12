class ContaBancaria:
    def __init__(self, nome, numero_conta, saldo):
        self.nome = nome
        self.numero_conta = numero_conta
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R${valor:.2f} realizado com sucesso.')
        else:
            print('Valor de depósito inválido.')

    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f'Saque de R${valor:.2f} realizado com sucesso.')
            else:
                print('Saldo insuficiente para saque.')
        else:
            print('Valor de saque inválido.')

    def consultar_saldo(self):
        print(f'Saldo atual: R${self.saldo:.2f}')

    def transferir(self, outra_conta, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                outra_conta.depositar(valor)
                print(f'Transferência de R${valor:.2f} realizada com sucesso para a conta de {outra_conta.nome}.')
            else:
                print('Saldo insuficiente para transferência.')
        else:
            print('Valor de transferência inválido.')