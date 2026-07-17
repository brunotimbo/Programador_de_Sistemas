lista = []

def calcular_media(l1):
    soma = 0
    for i in l1:
        soma += i
    return soma / len(l1)

while len(lista) < 5:
    numero = float(input("Digite o número: "))
    lista.append(numero)

print(calcular_media(lista))
