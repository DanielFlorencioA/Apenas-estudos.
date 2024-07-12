class Eevee:
    def __init__(self, apelido, pontos_vida, nivel):
        self.apelido = apelido
        self.pontos_vida = pontos_vida
        self.nivel = nivel

    def quick_attack(self):
        print('Você usou o ataque rápido')

    def bite(self):
        print('Esse é o ataque inútil --by Kayk')

class flareon(Eevee):
    def __init__(self, apelido, pontos_vida, nivel):
        super().__init__(apelido, pontos_vida, nivel)

flareon1 = flareon('Flareon', 40, 17)

flareon1.quick_attack()