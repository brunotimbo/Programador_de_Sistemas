print("\n")

opcao = int(input("Escolha a Opção (1-Ponte ou 2-Túnel): "))


if opcao == 1:

    blindado = str(input("Tem veículo blindado? "))
    ponte = str(input("Ponte intácta? "))

    if blindado == "sim" and ponte == "sim":
        print(f"Seguir pela Ponte.")

    else:
        print(f"Não siga pela Ponte.")


elif opcao == 2:

    mascara = str(input("Tem máscara de gás? "))
    cartao = str(input("Tem cartão de acesso? "))

    if mascara == "sim" and cartao == "sim":
        print(f"Seguir pelo Túnel.")  

    else:
        print(f"Não siga pelo Túnel.")

else:
    print(f"Opção inválida!")

