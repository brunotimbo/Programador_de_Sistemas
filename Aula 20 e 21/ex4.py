def eh_primo(n1):
    
    if n1 < 2:
        return f"\nO número {n1} NÃO é primo.\n"

    for i in range(2, n1):

        if n1 % i == 0:
            return f"\nO número {n1} NÃO é primo.\n"

    return f"\nO número {n1} É primo.\n"

numero = int(input("\nDigite um número para saber se é primo: "))

print(eh_primo(numero))

