frase = str(input("\nDigite uma frase: ")).replace(" ","")
total = 0

for i in frase:
    
    print(i)
    total += 1

print(f"\nO total de letras da frase é {total}")