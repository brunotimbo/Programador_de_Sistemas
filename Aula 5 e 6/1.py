print("\n")
ano_nascimento = int(input("Digite o ano do seu nascimento: "))

idade = 2026 - ano_nascimento

if idade >= 16:
    
    print("\n")
    print(f"Sua idade é {idade}. Pode Votar!")

else:

    print("\n")
    print(f"Sua idade é {idade}. Não Pode Votar!")