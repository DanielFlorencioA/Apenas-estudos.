texto = input("Digite um texto: ")

palavras = texto.lower().split()

contagem_palavras = {}

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1

print("Contagem de palavras no texto: ")
for palavra, quantidade in contagem_palavras.items():
    print("palavra: ", palavra, " quantidade: ", quantidade)