
class Televisao:
    # Método construtor
    # Método que 'adiciona uma linha à tabela'

    def __init__(self, marca, preco, modelo, menor_canal=2, maior_canal=25):
        self.marca = marca
        self.preco = preco
        self.modelo = modelo
        self.canal_atual = 100
        self.menor_canal = menor_canal
        self.maior_canal = maior_canal

    def passar_canal(self):
        if self.canal_atual == self.maior_canal:
            self.canal_atual = self.menor_canal
        else:
            self.canal_atual = self.canal_atual + 1

    def voltar_canal(self):
        if self.canal_atual == self.menor_canal:
            self.canal_atual = self.maior_canal
        else:
            self.canal_atual = self.canal_atual - 1
 # Instanciar uma classe
tv_sala = Televisao('Sansung', 3500, 'v8', 2, 100)

print(Televisao.canal_atual)
tv_sala.passar_canal()
print(tv_sala.canal_atual)


class Livro:
    def __init__(self, titulo, autor, ano_publicacao, disponivel = True):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
    
    def emprestar_livro(self):
        self.disponivel= False

    def devolver_livro(self):
        self.disponivel = True

    def exibir_detalhes(self):
        print(f'Titulo: {self.titulo}')
        print(f'Autor: {self.autor}')
        print(f'Ano de publicação: {self.ano_publicacao}')
        if self.disponivel:
            print(f'Disponível')
        else:
            print(f'indisponível')

primeiro_livro = Livro(' As duas torres', 'Tolkien', 1965)
primeiro_livro.emprestar_livro()
primeiro_livro.exibir_detalhes()