import sqlite3

conn = sqlite3.connect('UserData.bd')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Usuarios(
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Email TEXT NOTE NULL,
    telefone INTERGET, 
    Pais TEXT,
    Usuario TEXT NOT NULL, 
    senha TEXT NOT NULL
);
""")

print("Conectado ao Banco de Dados...")