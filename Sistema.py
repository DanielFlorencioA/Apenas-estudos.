import sqlite3
from tkinter import messagebox


class SistemaDeRegistro:

     def __init__(self):
          
        self.conn = sqlite3.connect("estudantes.db")
        self.c = self.conn.cursor()
        self.create_table()

     def create_table(self):
         
         self.c.execute('''CREATE TABLE IF NOT EXISTS estudantes(
                          id INTENGER PRIMARY KEY, 
                          nome TEXT NOT NULL,
                          email TEXT NOT NULL UNIQUE ) ''')
         
     def registro_estudantes(self, estudantes):
         
         self.c.execute("INSERT INTO estudantes(id, nome, email) VALUES(?,?,?) ", (estudantes))
         self.conn.commit()

         messagebox.showinfo('Sucesso', 'Registrado com sucesso!')

     def visualizar_estudantes(self):
         
         self.c.execute("SELECT * FROM estudantes")
         dados = self.c.fetchall()

         for i in dados:
             print(f"ID: {i[0]} Nome: {i[1]} email: {i[2]}")

     def procura_estudantes(self, id):
         
         self.c.execute("SELECT * FROM estudantes WHERE id=?", (id,))
         dados = self.c.fetchone()

         print(f"ID: {dados[0]} NOME: {dados[1]} EMAIL: {dados[2]}")

     def deleta_estudantes(self, id):
         
         self.c.execute("DELETE * FROM WHERE ID=?", (id,))
         self.conn.commit()

         messagebox.showinfo('Sucesso', f'Estudante com ID:{id} foi deletado!')

sistema_de_registro = SistemaDeRegistro()

estudante = ('João', 'joao@gmail.com')
sistema_de_registro.registro_estudantes(estudante)
         



          