
def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b



def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Divisão por zero"

'''    
def potenciacao(a, b):
    return a**b
'''

print(divisao(2, 0))


def converter(celsius):
    return adicao(multiplicacao(divisao(9, 5), celsius), 32)

print(converter(12))