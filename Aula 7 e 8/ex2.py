print("\n")
idade = int(input("Digite sua idade: "))
titulo = str(input("Você tem tìtulo de eleitor? "))

if idade >= 16 and titulo == "sim":
    
    print("\n")
    print(f"Pode votar.")

else:

    print("\n")
    print(f"Não pode votar.")
