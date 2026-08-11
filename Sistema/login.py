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
COR_BOTAO_TEXTO = "#000000"
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

    # cada create table precisa ser um execute separado
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS DISCIPLINA(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT NOT NULL
        )
    """)

    #cursor.execute("""
    #    CREATE TABLE IF NOT EXISTS TURMA(
    #    id INTEGER PRIMARY KEY AUTOINCREMENT,
    #    nome TEXT NOT NULL,
    #    curso_id INTEGER NOT NULL,
    #    aluno_id INTEGER NOT NULL,
    #    FOREIGN KEY (aluno_id) REFERENCES ALUNO(id)
    #    FOREIGN KEY (professor_id) REFERENCES PROFESSOR(id)
    #    FOREIGN KEY (curso_id) REFERENCES DISCIPLINA(id)
    #    )
    #""")

    conexao.commit()
    conexao.close()

######################  ADMINISTRADOR   ############################

def criar_admin_padrao():
# cria um admin padrão no banco, caso não exista
    conexao = bd.connect("sistema.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT COUNT(*) FROM ADMIN")
    total_admins = cursor.fetchone()[0]

    if total_admins == 0:
        cursor.execute("INSERT INTO ADMIN (usuario, senha) VALUES (?, ?)", ("admin","admin123"))
        conexao.commit()
    conexao.close()

def buscar_admin_banco(usuario, senha):

    print(usuario, senha)

    conexao = bd.connect("sistema.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM ADMIN WHERE usuario = ? AND senha = ?", (usuario,senha))
    resultado = cursor.fetchone()
    conexao.close()
    print(resultado)
    return resultado

def usuario_existe(usuario):
# verifica se já existe um admin cadastrado com esse usuário    
    conexao = bd.connect("sistema.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM ADMIN WHERE usuario = ?", (usuario,))
    resultado = cursor.fetchone()
    conexao.close()
    return resultado is not None

def salvar_admin_banco(usuario, senha):
# insere um novo admin no banco
    conexao = bd.connect("sistema.db")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO ADMIN (usuario, senha) VALUES (?,?)", (usuario, senha))
    conexao.commit()
    conexao.close()
    
def atualizar_admin_banco(id_admin, usuario, senha):
# atualiza usuário/senha de um admin existente
    conexao = bd.connect("sistema.db")
    cursor = conexao.cursor()
    cursor.execute("UPDATE ADMIN SET usuario = ?, senha = ? WHERE id = ?", (usuario, senha, id_admin))
    conexao.commit()
    conexao.close()

def deletar_admin_banco(id_admin):
# remove admin existente no banco pelo id
    conexao = bd.connect("sistema.db")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM ADMIN WHERE id = ?", (id_admin))
    conexao.commit()
    conexao.close()

######################  ALUNO   ############################

def buscar_aluno_banco():
# retorna todos os alunos cadastrados no banco
    conexao = bd.connect("sistema.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM ALUNO")
    resultado = cursor.fetchall
    conexao.close()
    return resultado

def salvar_aluno_banco(nome, email):
# insere novo aluno no banco
    conexao = bd.connect("sistema.db")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO ALUNO (nome, email) VALUES (?, ?)", (nome, email))
    conexao.commit()
    conexao.close()

def atualizar_aluno_banco(id_aluno, nome, email):
# atualiza dados de aluno no banco
    conexao = bd.connect("sistema.db")
    cursor = conexao.cursor()
    cursor.execute("UPDATE ALUNO SET nome = ?, email = ?, WHERE id = ?", (nome, email, id_aluno))
    conexao.commit()
    conexao.close()

def deletar_aluno_banco(id_aluno):
# apaga aluno do banco de dados pelo id
    conexao = bd.connect("sistema.db")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM ALUNO WHERE id = ?", (id_aluno))
    conexao.commit()
    conexao.close()

######################  PROFESSOR   ############################

def buscar_professor_banco():
# retorna todos os professores cadastrados no banco
    conexao = bd.connect("sistema.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM PROFESSOR")
    resultado = cursor.fetchall
    conexao.close()
    return resultado

def salvar_professor_banco(nome, email):
# insere novo professor no banco
    conexao = bd.connect("sistema.db")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO PROFESSOR (nome, email) VALUES (?, ?)", (nome, email))
    conexao.commit()
    conexao.close()

def atualizar_professor_banco(id_professor, nome, email):
# atualiza dados de professor no banco
    conexao = bd.connect("sistema.db")
    cursor = conexao.cursor()
    cursor.execute("UPDATE PROFESSOR SET nome = ?, email = ?, WHERE id = ?", (nome, email, id_professor))
    conexao.commit()
    conexao.close()

def deletar_professor_banco(id_professor):
# apaga professor do banco de dados pelo id
    conexao = bd.connect("sistema.db")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM PROFESSOR WHERE id = ?", (id_professor))
    conexao.commit()
    conexao.close()

######################  DISCIPLINA   ############################


def buscar_disciplina_banco():
# retorna todos as disciplinas cadastrados no banco
    conexao = bd.connect("sistema.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM DISCIPLINA")
    resultado = cursor.fetchall
    conexao.close()
    return resultado

def salvar_disciplina_banco(nome, descricao):
# insere nova disciplina no banco
    conexao = bd.connect("sistema.db")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO DISCIPLINA (nome, descricao) VALUES (?, ?)", (nome, descricao))
    conexao.commit()
    conexao.close()

def atualizar_disciplina_banco(id_disciplina, nome, descricao):
# atualiza dados de uma disciplina no banco
    conexao = bd.connect("sistema.db")
    cursor = conexao.cursor()
    cursor.execute("UPDATE DISCIPLINA SET nome = ?, descricao = ?, WHERE id = ?", (nome, descricao, id_disciplina))
    conexao.commit()
    conexao.close()

def deletar_disciplina_banco(id_disciplina):
# apaga disciplina do banco de dados pelo id
    conexao = bd.connect("sistema.db")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM DISCIPLINA WHERE id = ?", (id_disciplina))
    conexao.commit()
    conexao.close()

######################  INTERFACE   ############################

def limpar_janela():

# apaga todos os elementos da janela
    for widget in janela.winfo_children():
        widget.destroy()

def fazer_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    print(usuario, senha)
    if buscar_admin_banco(usuario, senha) is not None:
        messagebox.showinfo("Login", "Login efetuado com sucesso!")
    else:
        messagebox.showerror("Login", "Usuário ou senha incorretos!")

def fazer_cadastro():
    usuario_novo = entry_usuario_cadastro.get()
    senha_nova = entry_senha_cadastro.get()
    confirmacao = entry_senha_confirmar.get()

    print(usuario_novo, senha_nova, confirmacao)

    # validação 1: campos vazios
    if not usuario_novo or not senha_nova or not confirmacao:
        messagebox.showwarning("Cadastro", "Todos os campos devem ser preenchidos!")
        return

    # validação 2: comparar senhas
    if senha_nova != confirmacao:
        messagebox.showerror("Cadastro", "As senhas não coincidem!")
        return

    # validação 3: verificar se o usuário já existe no bd
    if usuario_existe(usuario_novo):
        messagebox.showerror("Cadastro", "Usuário já cadastrado!")
        return

    # se passou nas validações, salva novo admin no bd
    salvar_admin_banco(usuario_novo, senha_nova)
    messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")
    tela_login()


def tela_cadastro():
    # Informa ao Python que vamos modificar as variáveis globais nesta tela
    global entry_usuario_cadastro, entry_senha_cadastro, entry_senha_confirmar
    limpar_janela()
    janela.title("Cadastro")
    janela.geometry("300x350")

    # frame tela de cadastro
    frame_cadastro = tk.Frame(janela)
    frame_cadastro.pack(fill="both", expand=True)

    # título cadastro
    label_titulo = tk.Label(frame_cadastro, text="Cadastro", font=("Arial", 16))
    label_titulo.pack(pady=10)

    # texto campo usuário
    label_usuario = tk.Label(frame_cadastro, text="Usuário:")
    label_usuario.pack(pady=5)

    # campo usuário
    entry_usuario_cadastro = tk.Entry(frame_cadastro)
    entry_usuario_cadastro.pack(pady=5)

    # texto do campo senha
    label_senha = tk.Label(frame_cadastro, text="Senha:")
    label_senha.pack(pady=5)

    # campo senha
    entry_senha_cadastro = tk.Entry(frame_cadastro, show="*")
    entry_senha_cadastro.pack(pady=5)

    # texto do campo confirmar senha
    label_senha_confirmar = tk.Label(frame_cadastro, text="Confirmar senha:")
    label_senha_confirmar.pack(pady=5)

    # campo confirmar senha
    entry_senha_confirmar = tk.Entry(frame_cadastro, show="*")
    entry_senha_confirmar.pack(pady=5)

    # frame dos botões login e cadastro
    frame_botoes = tk.Frame(frame_cadastro)
    frame_botoes.pack(pady=10)

    # botões de login e cadastro
    botao_cadastrar = tk.Button(frame_botoes, text="Cadastrar", command=fazer_cadastro, bg=COR_BOTAO, fg=COR_BOTAO_TEXTO)
    botao_cadastrar.pack(side="left", pady=5, padx=10)
    botao_voltar = tk.Button(frame_botoes, text="Login", command=tela_login, bg=COR_BOTAO2, fg=COR_BOTAO_TEXTO)
    botao_voltar.pack(side="right", pady=5, padx=10)

def tela_login():
    global entry_usuario, entry_senha
    limpar_janela()
    janela.title("Login")
    janela.geometry("300x250")

    # frame da janela de login
    frame_login = tk.Frame(janela)
    frame_login.pack(fill="both", expand=True, ) 

    # título da tela de login
    label_titulo = tk.Label(frame_login, text="Sistema de Login", font=("Arial", 16))
    label_titulo.pack(pady=10)

    # texto do campo usuario
    label_usuario = tk.Label(frame_login, text="Usuário:", anchor="w",  width=17)
    label_usuario.pack(pady=5)

    # campo usuário
    entry_usuario = tk.Entry(frame_login)
    entry_usuario.pack(pady=5)

    # texto do campo senha
    label_senha = tk.Label(frame_login, text="Senha:")
    label_senha.pack(pady=5)

    # campo senha
    entry_senha = tk.Entry(frame_login, show="*")
    entry_senha.pack(pady=5)

    # frame dos botões login e cadastro
    frame_botoes = tk.Frame(frame_login)
    frame_botoes.pack(pady=10)

    # botões de login e cadastro
    botao_login = tk.Button(frame_botoes, text="Login", command=fazer_login, bg=COR_BOTAO, fg=COR_BOTAO_TEXTO)
    botao_login.pack(side="left", pady=5, padx=10)
    botao_cadastro = tk.Button(frame_botoes, text="Cadastrar Admin", command=tela_cadastro, bg=COR_BOTAO2, fg=COR_BOTAO_TEXTO)
    botao_cadastro.pack(side="right", pady=5, padx=10)

# PREPARA BD ANTES DE ABRIR A JANELA
conectar_banco()
criar_admin_padrao()

# CRIA JANELA PRINCIPAL
janela = tk.Tk()
janela.title("Login")
janela.geometry("300x250")
janela.resizable(False, False)
tela_login()
janela.mainloop()














