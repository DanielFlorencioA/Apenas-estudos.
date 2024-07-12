#Desenvolvido por Prô Terra - MakerZine
#Para mais detalhes, acesse: https://www.makerzine.com.br

nome = input("Digite seu login: ")
senha = input("Digite sua senha: ")

while nome == senha:
    print("Erro: A senha não deve ser igual ao nome")
    senha = input("Digite sua senha: ")
print("Login Ok")