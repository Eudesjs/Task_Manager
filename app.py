
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row 
    return conn

def init_db():
    conn = get_db_connection()  
    conn.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT
        )
    ''')  
    conn.commit()  
    conn.close()   

@app.route('/')
def index():
    conn = get_db_connection()  
    tasks = conn.execute('SELECT * FROM tasks').fetchall()  
    conn.close()  
    return render_template('index.html', tasks=tasks)  

@app.route('/add', methods=('GET', 'POST'))
def add_task():
    if request.method == 'POST': 
        title = request.form['title']  
        description = request.form['description'] 
        
        if title:  
            conn = get_db_connection()
            conn.execute('INSERT INTO tasks (title, description) VALUES (?, ?)',
                         (title, description))  
            conn.commit() 
            conn.close()  
            return redirect(url_for('index'))  
    
    return render_template('add_task.html')  

@app.route('/edit/<int:id>', methods=('GET', 'POST'))
def edit_task(id):
    conn = get_db_connection()
    task = conn.execute('SELECT * FROM tasks WHERE id = ?', (id,)).fetchone()  

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        
        if title:
            conn.execute('UPDATE tasks SET title = ?, description = ? WHERE id = ?',
                         (title, description, id))  
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    
    conn.close()
    return render_template('edit_task.html', task=task)  

@app.route('/delete/<int:id>', methods=('POST',))
def delete_task(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?', (id,))  
    conn.commit()
    conn.close()
    return redirect(url_for('index'))  

if __name__ == '__main__':
    init_db()  
    app.run(debug=True)  
