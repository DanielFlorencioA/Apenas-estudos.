import random

print("Iniciando jogo!")
print("Boa sorte!")

    
def gerar_palpite():
    numeros = random.randint(1,100)
    palpite = 0
    tentativas = 0
    
    while palpite != numeros:
        tentativas +=1
        palpite = int(input("Digite um valor entre 1 e 100: "))


        if palpite == numeros:
            print("Parabéns!", "Voce acertou em: ", tentativas,"Tentativas ", "O número é: ", numeros)
        elif palpite > numeros:
            print("Número devi ser menor.Tente novamente!")
        elif palpite < numeros:
            print("Número devi ser maior.Tente novamente!")
        else:
            print("Suas tentativas acabaram!")

gerar_palpite() 

            

    
        

    

        
    