import random

palavras = [
    'lagosta',
    'hiena',
    'jabuti',
    'atum',
    'guaxinim',
    'lhama',
    'lagarto',
    'peixe-betta',
    'ganso',
    'lula',
    ]
nome = 'juliano'
print(nome.upper())

alfabeto = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z',
]

def escolher_palavra_aleatoria():
    palavra = random.choice(palavras)
    return palavra

def digitar_uma_palavra():
    palavra = input('Digite a palavra que deseja: ')
    return palavra.lower()

def achou_letra_no_alfabeto(letra_escolhida):
    for letra in alfabeto:
        if letra == letra_escolhida:
            return True
    else:
        return False

def achou_letra_na_palavra(letra_escolhida, palavra):
    for letra in palavra:
        if letra == letra_escolhida:
            return True
    else:
        return False
    
def criar_espacos_em_branco(letras_escolhidas, palavra):
    resultado = ''
    contador_de_vitoria = 0
    for letra in palavra:
        if letra in letras_escolhidas or letra == '-':
            resultado = resultado + letra
        else:
            contador_de_vitoria += 1
            resultado = resultado + '_'
    return [resultado, contador_de_vitoria]

def menu_escolha_palavra():
    palavra = ''
    while True:
        print('1 - Palavra aleatória')
        print('2 - Escreva sua própria palavra')
        opcao = input('Escolha uma opção (0 para sair): ')
        if opcao == '1':
            palavra = escolher_palavra_aleatoria()
            break
        elif opcao == '2':
            palavra = digitar_uma_palavra()
            break
        elif opcao == '0':
            break
    return palavra

def verificao_letra_palavra(letras_escolhidas, palavra_escolhida, vidas):
    while True:
        print(10*'=')
        resultado_atual = criar_espacos_em_branco(letras_escolhidas, palavra_escolhida)
        print(resultado_atual[0])
        if resultado_atual[1] == 0:
            print('Parabéns, você venceu!')
            break
        letra = input('Digite uma letra do alfabeto: ').lower()
        if achou_letra_no_alfabeto(letra) and letra not in letras_escolhidas:
            letras_escolhidas.append(letra)
            if not achou_letra_na_palavra(letra, palavra_escolhida):
                vidas -= 1
                print('A letra não existe na palavra\nVocê perdeu uma vida!')
                if vidas == 0:
                    print('Não lhe restam mais vidas!')
                    print(f'A palavra era {palavra_escolhida}')
                    break
                else:
                    print(f'Agora lhe restam {vidas} vidas')
        elif letra in letras_escolhidas:
            print('A letra já foi escolhida')
        else:
            print('Por favor digite apenas letras')
        print(10*'=')


while True:
    palavra_escolhida = menu_escolha_palavra()
    letras_escolhidas = []
    vidas = 5
    verificao_letra_palavra(letras_escolhidas, palavra_escolhida, vidas)
    break