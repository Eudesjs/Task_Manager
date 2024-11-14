# Importa as bibliotecas necessárias para a aplicação
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

# Cria uma aplicação Flask
app = Flask(__name__)

# Função para conectar ao banco de dados SQLite
def get_db_connection():
    # Conecta ao arquivo 'database.db' e retorna a conexão
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row  # Permite acessar os dados por nome das colunas
    return conn

# Função para criar a tabela de tarefas, se não existir
def init_db():
    conn = get_db_connection()  # Conecta ao banco
    conn.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT
        )
    ''')  # Cria a tabela com campos 'id', 'title' e 'description'
    conn.commit()  # Salva as mudanças
    conn.close()   # Fecha a conexão

# Página principal que lista todas as tarefas
@app.route('/')
def index():
    conn = get_db_connection()  # Conecta ao banco
    tasks = conn.execute('SELECT * FROM tasks').fetchall()  # Busca todas as tarefas
    conn.close()  # Fecha a conexão
    return render_template('index.html', tasks=tasks)  # Renderiza o template com as tarefas

# Página para adicionar uma nova tarefa
@app.route('/add', methods=('GET', 'POST'))
def add_task():
    if request.method == 'POST':  # Se o formulário for enviado
        title = request.form['title']  # Recebe o título
        description = request.form['description']  # Recebe a descrição
        
        if title:  # Verifica se o título foi preenchido
            conn = get_db_connection()
            conn.execute('INSERT INTO tasks (title, description) VALUES (?, ?)',
                         (title, description))  # Insere a tarefa no banco
            conn.commit()  # Salva as mudanças
            conn.close()  # Fecha a conexão
            return redirect(url_for('index'))  # Redireciona para a página principal
    
    return render_template('add_task.html')  # Exibe o formulário para adicionar tarefa

# Página para editar uma tarefa existente
@app.route('/edit/<int:id>', methods=('GET', 'POST'))
def edit_task(id):
    conn = get_db_connection()
    task = conn.execute('SELECT * FROM tasks WHERE id = ?', (id,)).fetchone()  # Busca a tarefa pelo 'id'

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        
        if title:
            conn.execute('UPDATE tasks SET title = ?, description = ? WHERE id = ?',
                         (title, description, id))  # Atualiza a tarefa no banco
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    
    conn.close()
    return render_template('edit_task.html', task=task)  # Exibe o formulário para editar a tarefa

# Função para deletar uma tarefa
@app.route('/delete/<int:id>', methods=('POST',))
def delete_task(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?', (id,))  # Deleta a tarefa do banco
    conn.commit()
    conn.close()
    return redirect(url_for('index'))  # Redireciona para a página principal

# Inicializa o banco de dados antes de rodar a aplicação
if __name__ == '__main__':
    init_db()  # Cria a tabela se ela ainda não existe
    app.run(debug=True)  # Inicia o servidor em modo debug
