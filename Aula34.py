import sqlite3

class BancodedadosSQlite:

    def __init__(self, nome_titular, numero_conta, saldo_inicial=0):
        self.nome_titular = nome_titular
        self.numero_conta = numero_conta
        self.saldo = saldo_inicial

# Criando a "class" do estoque
class Contabancaria:

    def __init__(self, db_name="banco.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.create_table()

# Criando a tabela é específicando como quero que cada item seja digitado
    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS  (
                          
                        )''')
        self.conn.commit()


 
