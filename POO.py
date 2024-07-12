class ContaBancaria:

    def __init__(self, nome_titular, numero_conta, saldo_inicial=0):
        self.nome_titular = nome_titular
        self.numero_conta = numero_conta
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Valor depositado R$ {valor}")
        else: 
            print("Valor do depósito inválido")
    
    def sacar(self, valor):
        if valor > 0:
            if  self.saldo >= valor:
                self.saldo -= valor
                print(f"Saque no valor de R$ {valor} realizado com sucesso!")
            else:
                print("Valor de saque inválido!")
        else:
            print("O valor do saque deve ser maior que zero!")

    def consultar(self):
        return self.saldo
    
    def transferir(self, valor, outra_conta):
        if valor > 0:
            if  self.saldo >= valor:
                self.saldo -= valor
                outra_conta.depositar(valor)
                print(f"Transferencia no valor de  R$ {valor} para a conta {outra_conta.numero_conta} realizado com sucesso!")
            else:
                print("Saldo insuficiente!")
        else:
            print("O valor da transferencias deve ser maior que zero!")

conta1 = ContaBancaria("João", "123456")
conta2 = ContaBancaria("Maria", "67890", 1000)

print("Saldo inicial da conta de João: ", conta1.consultar())
print("Saldo inicial da conta de Maria: ", conta2.consultar())

conta1.depositar(500)
conta1.sacar(200)
conta1.transferir(100, conta2)


            
        
    


       