import tkinter as tk
import sqlite3

janela = tk.Tk()
janela.title("Componentes Básicos")
janela.geometry("300x400")

def exibir_nome():
    nome = entry_nome.get()
    idade = int(entry_idade.get())
    curso = entry_curso.get()

    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Alunos (
        ID INTERGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT,
        Idade INTEGER,
        Curso TEXT)
    ''')
    conexao.commit()
    cursor.execute('''INSERT INTO Alunos (
        Nome, Idade, Curso)
        VALUES (?, ?, ?)''', (nome, idade, curso)
    )
    conexao.commit()

# Criando um Frame para agrupar o conteúdo
frame_centro = tk.Frame(janela)

# Centraliza o frame no centro da janela
frame_centro.pack(expand=True)

# Label nome e campo nome
label_nome = tk.Label(frame_centro, text = "Digite o nome:")
label_nome.pack()
entry_nome = tk.Entry(frame_centro)
entry_nome.pack()

# Label idade e campo idade
label_idade = tk.Label(frame_centro, text = "Digite a idade:")
label_idade.pack()
entry_idade = tk.Entry(frame_centro)
entry_idade.pack()

# Label curso e campo curso
label_curso = tk.Label(frame_centro, text="Digite o curso:")
label_curso.pack()
entry_curso = tk.Entry(frame_centro)
entry_curso.pack()

# Botão enviar
button = tk.Button(frame_centro, text="Enviar", command=exibir_nome)
button.pack()

janela.mainloop()