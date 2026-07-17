dicionario = {
"field": "Campo",
"room": "Quarto",
"match": "Partida",
"breathtaking": "De tirar o fôlego",
"overwhelmin": "Esmagador",
"awkward": "Estranho",
"actually": "Na verdade",
"pretend": "Fingir",
"push": "Empurrar"}

while True:

    palavra = input("\nDigite ama palavra em inglês para traduzir para português: ")
    palavra_minuscula = palavra.lower()

    if palavra_minuscula in dicionario:
        print(f"{palavra} em português significa {dicionario[palavra_minuscula]}.")
    else:
        print("Esta palavra não consta na lista. Tente outra.")