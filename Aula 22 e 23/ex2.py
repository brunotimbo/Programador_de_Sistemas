dicionario_pessoa = {
    "nome": "Bruno",
    "idade": 37,
    "cidade": "Fortaleza",
    "profissão": "Autônomo"
}

def exibe(par):
    print(f"O nome é {dicionario_pessoa[par]}.")

def exibe_menu():
        print("""\n====== MENU ======\n
O que deseja cosultar?
1. Nome
2. Idade
3. Cidade
4. Profissão
0. Sair""")
    
        opcao = int(input("\nEscolha a opção: "))    
        return opcao

def verifica_opcao(par):
    if par == 1:
        exibe("nome")
    elif par == 2:
        exibe("idade")
    elif par == 3:
        exibe("cidade")
    elif par == 4:
        exibe("profissão")
    elif par == 0:
        print("Fim")
    else:
        print("Opção inválida!")

while True:
    verifica_opcao(exibe_menu())
        