import sqlite3

conn = sqlite3.connect('banco.db')

conn.execute('''
CREATE TABLE IF NOT EXISTS usuarios (    
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL UNIQUE,
    nome TEXT NOT NULL,
    senha TEXT NOT NULL
)
''')