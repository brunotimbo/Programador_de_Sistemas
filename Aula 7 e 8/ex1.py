print("\n")
idade = int(input("Digite sua idade: "))
cnh = str(input("Você tem habilitação? "))

if idade >= 18 and cnh == "sim":
    
    print("\n")
    print(f"Pode dirigir!")

else:

    print("\n")
    print(f"Não pode dirigir!")
