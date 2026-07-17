dicionario_amigos = {
    "João": {"idade": 25, "cidade": "Fortaleza", "telefone": "8599999999"},
    "Maria": {"idade": 28, "cidade": "Caucaia", "telefone": "85988888888"},
    "Pedro": {"idade": 22, "cidade": "Maracanaú", "telefone": "85977777777"},
    "Ana": {"idade": 50, "cidade": "Pacatuba", "telefone": "859666666"}
}
while True:

    nome = input("Digite o nome do amigo: ")

    if nome in dicionario_amigos:
        print(f"{dicionario_amigos[nome]}\n")
    else:
        print("Nome não encontrado.\n")