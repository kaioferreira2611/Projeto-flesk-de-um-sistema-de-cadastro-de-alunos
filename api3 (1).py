from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Função que cria o banco se não existir
def init_db():
    conn = sqlite3.connect('alunos.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Página inicial - lista de alunos
@app.route('/')
def index():
    conn = sqlite3.connect('alunos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM alunos')
    alunos = cursor.fetchall()
    conn.close()
    return render_template('index.html', alunos=alunos)

# Cadastro de aluno
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']

        conn = sqlite3.connect('alunos.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO alunos (nome, idade) VALUES (?, ?)', (nome, idade))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('cadastro.html')


if __name__ == '__main__':
    app.run(debug=True)
