import random

print("\n")

n1 = random.randint(1, 10)

n2 = int(input("Digite um número: "))

while n1 != n2:

    if n1 > n2:
        print("\n")
        n2 = int(input("O número é MAIOR. Digite novamente: "))

    elif n1 < n2:
        print("\n")
        n2 = int(input("O número é MENOR. Digite novamente: "))

print("\n")
print ("Acertou!")   
