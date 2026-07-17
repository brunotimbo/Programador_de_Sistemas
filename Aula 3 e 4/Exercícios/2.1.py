print("\n")
altura = float(input("Digite sua altura(m): "))
peso = float(input("Digite seu peso(Kg): "))

imc = peso / (altura**2)

print("\n")
print(f"Seu IMC é {imc:.2f}.")
