dicionario_pessoa = {
    "nome": "Bruno",
    "idade": 37,
    "cidade": "Fortaleza",
    "profissão": "Autônomo",
    "telefone": "85999999999"
}

def exibe_dicionario():
    print(dicionario_pessoa)

def exibe_menu():
    print("""\n====== MENU ======\n
Qual valor deseja excluir?
1. Nome
2. Idade
3. Cidade
4. Profissão
5. Telefone""")
        
    opcao = input("\nEscolha a opção: ")    
    return opcao

def verifica_opcao(op):
    if op == "1":
        return "nome"
    elif op == "2":
        return "idade"
    elif op == "3":
        return "cidade"
    elif op == "4":
        return "profissão"
    elif op == "5":
        return "telefone"
    else:
        return "Opção inválida!\n"

def exclui_chave(chave):
    if chave in dicionario_pessoa:  
        del dicionario_pessoa[chave]
        print(f"Chave {chave} DELETADA!\n")
    else:
        print(chave)

while True:
    exclui_chave(verifica_opcao(exibe_menu()))
    exibe_dicionario()
