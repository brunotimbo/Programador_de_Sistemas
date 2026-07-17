dicionario = {
    "celular": 0,
    "notebook": 2,
    "computador": 8,
    "tablet": 6,
    "mouse": 1,
    "teclado": 12,
    "monitor": 14
}

while True:
    produto = input("\nDigite o produto para saber a quantidade: ")

    if produto in dicionario:

        if dicionario[produto] > 1:
            print(f"Há {dicionario[produto]} unidades de {produto} no estoque.")

        else:
            print("Produto em falta.")

    else:
        print("Produto não cadastrado.")