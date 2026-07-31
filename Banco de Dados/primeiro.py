import sqlite3

# Conecta ao banco de dados (ou criar um novo)
conexao = sqlite3.connect('exemplo.db')

# Cria um cursor para interagir com o banco de dados
cursor = conexao.cursor()

# Criar a tabela Alunos
# cursor.execute('''
# CREATE TABLE Alunos(
# ID INTEGER PRIMARY KEY,
# Nome TEXT NOT NULL,
# Idade INTEGER,
# Curso TEXT
# )
# ''')
# # Confirmar a transação
# conexao.commit()

cursor.execute('''
INSERT INTO Alunos (Nome, Idade, Curso)
VALUES ('Ana', 21, 'Engenharia'),
        ('Bruno', 22, 'Direito'),
        ('Carla', 20, 'Medicina')
''')

#confirma a transação
conexao.commit()

# Inserir dados na tabela

def inserir_dados(nome, idade, curso):
    
        cursor.execute('''INSERT INTO Alunos (Nome, Idade, Curso)
        VALUES (?, ?, ?)''', (nome, idade, curso))

        # Confirmar a transação
        conexao.commit()

nome = input("Qual seu nome: ")
idade = int(input("Qual sua idade: "))
curso = input("Qual seu curso: ")
inserir_dados(nome, idade, curso)