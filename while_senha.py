count = 0
senha = int(input("Digite a senha: "))

while True:

    if senha == "1234":
        print("Seja bem vindo")
        break
    else:
        count += 1
        if count < 3:
            print("Acesso negado!")
            senha = input("Tente novamente: ")
        else:
            print("Acesso bloqueado!")
            break
print("Fim")        
