class Pessoa:
    nome = ""
    idade = 0
    peso = 0.0
    altura = 0.0

    def __init__(self, nome, idade, peso, altura):
        self.nome = nome 
        self.idade = idade
        self.peso = peso
        self.altura = altura

    
    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.altura += 0.5

    def engordar(self):
        s

        

    