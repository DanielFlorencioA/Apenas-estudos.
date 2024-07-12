from flask import Flask, render_template, request, redirect, url_for
import csv
import os

app = Flask(__name__)

# Verifica se o arquivo CSV de usuários existe, se não, cria um novo
if not os.path.exists('users.csv'):
    with open('users.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['username', 'password'])

# Função para verificar se um usuário está registrado
def is_registered(username):
    with open('users.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username:
                return True
    return False

# Função para verificar as credenciais do usuário
def check_credentials(username, password):
    with open('users.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username and row['password'] == password:
                return True
    return False

# Rota para a página de login
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if check_credentials(username, password):
            return redirect(url_for('dashboard', username=username))
        else:
            return render_template('login.html', message='Credenciais inválidas. Tente novamente.')
    return render_template('login.html', message='')

# Rota para o painel do usuário
@app.route('/dashboard/<username>')
def dashboard(username):
    return render_template('dashboard.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
