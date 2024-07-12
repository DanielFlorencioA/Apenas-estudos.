class Livro:

    def __init__(self, titulo, autor, genero, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.disponivel = disponivel

class Menbro:

    def __init__(self, nome, id):
        self.nome = nome
        self.id = id
        self.livros_emprestado = []

class Biblioteca:

    def __init__(self):
         self.livros = []
         self.menbros = []
         

    def adicionar(self, livro):

        self.Livros.append(livro)
        print("Livro adicionado com sucesso!")

    def emprestar_livro(self, livro, membro):

        if livro in self.livros and livro.disponivel:
            membro.emprestar_livro(livro)
        elif livro.disponivel == False:
            print("Este livro não está disponivel para empréstimo.")
        else:
            print("Este livro não está na biblioteca.") 
            

    def devolver(self, livro):
        if livro 
        


    

