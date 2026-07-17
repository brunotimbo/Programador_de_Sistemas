dicionario_pessoa = {
    "nome": "Bruno",
    "idade": 37,
    "cidade": "Fortaleza",
    "profissão": "Autônomo"
}

def exibe_menu():
        print("""\n====== MENU ======\n
Qual valor deseja alterar?
1. Nome
2. Idade
3. Cidade
4. Profissão
0. Sair""")
        
        opcao = input("\nEscolha a opção: ")    
        return opcao

def exibe_dicionario():
        print(dicionario_pessoa)

def modificar_valor(op):

        if op == "1":
                dicionario_pessoa["nome"] = input("Digite o novo nome: ")
                print("Nome atualizado.\n")

        elif op == "2":
                dicionario_pessoa["idade"] = input("Digite a nova idade: ")
                print("Idade atualizada.\n")
        elif op == "3":
                dicionario_pessoa["cidade"] = input("Digite a nova cidade: ")
                print("Cidade atualizada.\n")
                     
        elif op == "4":
                dicionario_pessoa["profissão"] = input("Digite a nova profissão: ")
                print("Profissão atualizada.\n")

        elif op == "5":
                print("Fim\n")      
                
        else:
                print("Opção inválida!\n")                

while True:        
        modificar_valor(exibe_menu())
        exibe_dicionario()  