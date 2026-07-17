print("\n")
combustivel = float(input("Porcentagem do combustível: "))
atmosfera = str(input("A atmosfera do planeta é respirável? "))
traje = float(input("Porcentagem de integridade do traje de biosegurança: "))

if combustivel <= 15 and (atmosfera == "sim" or traje == 100):
    
    print("\n")
    print(f"Iniciando Protocolo de Pouso.")

else:

    print("\n")
    print(f"Pouso Abortado: Risco de Morte")
