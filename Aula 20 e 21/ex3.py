def contar_vogais(f1):
    
    contador = 0
    vogais = "aeiouAEIOU"
    
    for i in f1:
        if i in vogais:
            contador += 1
    
    if contador <= 1:
        print(f"\nEsta frase tem {contador} vogal.\n")

    else:
        print(f"\nEsta frase tem {contador} vogais.\n")

frase = str(input("\nDigite uma frase: "))

contar_vogais(frase)