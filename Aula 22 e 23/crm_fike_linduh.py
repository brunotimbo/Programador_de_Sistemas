clientes = {
    "12345678901": {"nome": "Ana Silva", "idade": 28, "compras": [120.50, 89.90, 45.00], "categoria": "VIP"},
    "98765432100": {"nome": "Bruno Costa", "idade": 34, "compras": [350.00, 500.00], "categoria": "Premium"},
    "45678912344": {"nome": "Carla Souza", "idade": 22, "compras": [50.00], "categoria": "Regular"},
    "78912345655": {"nome": "Diego Lima", "idade": 41, "compras": [15.00, 30.00, 25.50, 40.00], "categoria": "Regular"}
    }

#buscar cliente por cpf
while True:
    cpf = input("\nDigite o cpf do cliente: ")

    if cpf in clientes:      

        print(f"""
Nome: {clientes[cpf]["nome"]} 
Idade: {clientes[cpf]["idade"]}
Total Compras: R${sum(clientes[cpf]["compras"]):.2f}
Categoria: {clientes[cpf]["categoria"]}"""
        )
    
    else:
        print("CPF não cadastrado.")

#atualizar regular para vip
