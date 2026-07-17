dicionario_pessoa = {
    "nome": "Bruno",
    "idade": 37,
    "cidade": "Fortaleza",
    "profissão": "Autônomo"
}

def exibe_dicionario():
    print(dicionario_pessoa)

def exibe_menu():
        print("""\n====== MENU ======\n
Qual novo valor deseja incluir ?
1. Telefone
2. Email""")
        
        opcao = input("\nEscolha a opção: ")    
        return opcao

def adicionar_chave(op):

    if op == "1":
        telefone = input("Digite o telefone: ")
        dicionario_pessoa["telefone"] = telefone
        print("Telefone adicionado\n")

    elif op == "2":
        email = input("Digite o email: ")
        dicionario_pessoa["email"] = email
        print("Email adicionado\n")

    else:
        print("Opção inválida!\n")

while True:
    adicionar_chave(exibe_menu())
    exibe_dicionario()    