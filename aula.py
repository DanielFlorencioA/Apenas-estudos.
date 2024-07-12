'''
class ContaBancaria:
    def __init__(self, saldo, nome_dono, numero_conta):
        self.__saldo = saldo
        self.nome_dono = nome_dono
        self.numero_conta = numero_conta

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, novo_saldo):
        if novo_saldo < 0:
            return False
        else:
            self.__saldo = novo_saldo
    
    def set_nome_dono(self, novo_nome):
        self.__nome_dono = novo_nome

    def get_numero_conta(self):
        return self.__numero_conta 

nova_conta = ContaBancaria(0, 'André', '1')

nova_conta.set_saldo(-500)

print(nova_conta.get_saldo())

nova_conta.set_saldo(1500)
'''