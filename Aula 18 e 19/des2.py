lista = []
lista_par = []
lista_impar = []


for i in range(20):

    valor = int(input("Digite um valor: "))
    lista.append(valor)

for i in range(len(lista)):

    if lista[i] % 2 == 0:
        lista_par.append(lista[i])
    else:
        lista_impar.append(lista[i])    

print(f"\nLista de números pares: {lista_par}")
print(f"Lista de números ímpares: {lista_impar}")