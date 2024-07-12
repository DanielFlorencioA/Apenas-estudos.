print("1- cadastro")
print("2-login")
escolha = input("Digite sua escolha (1 or 2): ")
if escolha in ('1', '2',):

 if escolha == '1':
  print('Olá, aqui você pode adicionar uma nova conta!')
  nome_cadastro = input("Digite seu nome: ")
  senha = input("Digite sua senha: ")
  cpf = int(input("Digite seu cpf: "))
 print("cadastro feito")

 while True: 
    try: 
        senha = int(input("Informe a nota entre 0 e 10: ")) 
        if not 0 <= senha <= 10: 
            raise ValueError("Nota fora do range permitido") 
    except ValueError as e: 
        print("Valor inválido:", e) 
    else: 
        break 
 


arquivo = open("registrados.txt", "a")
arquivo.close()

arquivo = open("registrados.txt")
if escolha == '2':
 print('Efetue o seu login')
nome_login = input("Digite o seu nome de usúario: ")
senha_login = input("Digite sua senha de usúario: ")
cpf_login = input("Digite seu cpf de usúario: ")
arquivo.close()

print("Bem vindo!")

