lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#tamanho = len(lista)

for i in range(len(lista)):
    if lista[i] % 2 == 0:
        lista[i] = 0

print(lista)
