import tkinter as tk
import tkinter.messagebox as messagebox
import sqlite3 as bd

# variáveis globais para campos de texto
entry_usuario = None
entry_senha = None
entry_usuario_cadastro = None
entry_senha_cadastro = None
entry_senha_confirmar = None

# cores padrão
COR_FUNDO = "#FFFFFF"
COR_TEXTO = "#000000"
COR_BOTAO = "#4CAF50"
COR_TEXTO_BOTAO = "#000000"
COR_BOTAO2 = "#FFA500"

def conectar_banco():

    # cria banco de dados e tabelas caso não existam
    conexao = bd.connect("sistema.db")
    cursor = conexao.cursor()

    # cada create table precisa ser um execute separado
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ADMIN(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT NOT NULL,
        senha TEXT NOT NULL
        )
    """)

    # cada create table precisa ser um execute separado
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ALUNO(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
            )
    """)

    # cada create table precisa ser um execute separado
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS PROFESSOR(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS TURMA(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        curso_id INTEGER NOT NULL,
        aluno_id INTEGER NOT NULL,
        FOREIGN KEY (aluno_id) REFERENCES ALUNO(id)
        FOREIGN KEY (professor_id) REFERENCES PROFESSOR(id)
        FOREIGN KEY (curso_id) REFERENCES DISCIPLINA(id)
        )
    """)

    conexao.commit()
    conexao.close()

######################ADMINISTRADOR############################

def criar_admin_padrao():

    # cria um admin padrão no banco, caso não exista
    conexao = bd.connect("sistema.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT COUNT(*) FROM ADMIN")
    total_admins = cursor.fetchone()[0]

    if total_admins == 0:
        cursor.execute(
            "INSERT INTO ADMIN (usuario, senha) VALUES (?, ?)",
            ("admin","admin123")
        )
        conexao.commit()
    conexao.close()

def buscar_admin_banco(usuario, senha):

    conexao = bd.connect("sistema.db")
    cursor = conexao.cursor()
    cursor.execute(
        "SELECT * FROM ADMIN WHERE usuario = ? AND senha = ?",
        ("usuario","senha")
    )
    resultado = cursor.fetchone()
    conexao.close()
    return resultado