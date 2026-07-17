convidados = ["Bruno", "Luisa", "Lima", "Ana"]

while True:

    opcao = int(input("""\n============= MENU =============\n
1. Adicionar convidado" 
2. Listar convidados 
3. Consultar convidado 
4. Remover convidado 
5. Quantidade de convidados 
6. Editar convidado 
0. Sair\n
Digite a opção: """))

    if opcao == 1:
        print("\nADICIONAR CONVIDADO")
        while True:            
            nome = input("\nDigite o nome a ser adicionado ('0' para voltar): ")
            
            if nome == "0":
                break
                  
            convidados.append(nome)
            print("Nome incluido na lista.")            

    elif opcao == 2:
        print("\nLISTA DE CONVIDADOS\n")
        while True:        
            
            for i in convidados:
                count = convidados.index(i) + 1
                print(f"{count} - {i}")

            voltar = input("\n'0' para voltar: ")
            if voltar == '0':
                break

    elif opcao == 3:
        print("\nCONSULTAR CONVIDADO")
        while True:
            
            nome = input("\nDigite o nome a ser consultado ('0' para voltar): ")
            
            if nome == '0':
                break

            if nome in convidados:
                print(f"{nome} está na lista.")
            else:
                print(f"{nome} não está na lista.")



    elif opcao == 4:
        print("\nREMOVER CONVIDADO")
        while True:
            
            nome = input("\nDigite o nome a ser removido ('0' para voltar): ")

            if nome == '0':
                break
            
            if nome in convidados:
                convidados.remove(nome)
                print(f"{nome} foi removido(a) da lista.")
            else:
                print("Nome não encontrado na lista.")

    elif opcao == 5:
        
        while True:
            
            print(f"\nQUANTIDADE DE CONVIDADOS\n\nA lista possui {len(convidados)} convidados.")

            voltar = input("'0' para voltar: ")
            
            if voltar == '0':
                break
        
    elif opcao == 6:
        print("\nEDITAR CONVIDADO")
        while True:            
            nome = input("\nDigite o nome a ser editado ('0' para voltar): ")

            if nome == '0':
                break

            if nome in convidados:
                posicao = convidados.index(nome)
                nome_novo = input("Digite o novo nome: ")
                convidados[posicao] = nome_novo
                print(f"\n{nome} foi alterado para {nome_novo}.")
            else:
                print(f"{nome} não está na lista.")
        
    else:
        print("\nFIM")
        break

