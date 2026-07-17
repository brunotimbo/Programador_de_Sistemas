print("\n")
compra = float(input("Digite o valor da compra: "))
vip = str(input("Você é cliente VIP? "))

if compra >= 100 or vip == "sim":
    
    print("\n")
    print(f"Desconto de 10%. Valor a pagar R$ {compra - compra * 0.10}")

else:

    print("\n")
    print(f"Não tem desconto.")
