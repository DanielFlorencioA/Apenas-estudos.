notas = []
aluno = int(input('Qual o numero de alunos ? '))
for i in range(1,aluno + 1):
    print(aluno)

    for j in range(1,4):
        nota = float(input("Digite nota 1: "))
        notas.append(nota)  
        nota2 = float(input("Digite nota 2: "))
        notas.append(nota2)
        nota3 = float(input("Digite nota 3: "))
        notas.append(nota3)
        soma = sum(notas)
        media = soma / len(notas)
        print("A média das notas do aluno 1 é:", media)
