class Estudante:
    def __init__(self):
        self.informacoes = {}

    def adicionar_informacoes(self, chave, valor):
        self.informacoes[chave] = valor

    def adicionar_notas(self, notas):
        self.informacoes["notas"] = notas

    def calcular_media(self):
        notas = self.informacoes.get("notas", [])
        if notas:
            return sum(notas/len(notas))
        else:
            return "Nenhuma nota disponível!"
        
    def exibir_informacoes(self):
        print("Informações do Estudante: ")
        for chave, valor in self.informações.items():
            print(f"{chave.capitalize()}: {valor}")
    

estudante1 = Estudante()
estudante1.adicionar_informacoes("nome", "João")
estudante1.adicionar_informacoes("Idade", 20)
estudante1.adicionar_informacoes("Curso", "Técnico em Informática")
estudante1.adicionar_notas([8, 7, 9, 10])
    
        