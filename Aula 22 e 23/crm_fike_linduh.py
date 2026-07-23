clientes = {
    "12345678901": {"nome": "Ana Silva", "idade": 28, "compras": [120.50, 89.90, 45.00], "categoria": "VIP"},
    "98765432100": {"nome": "Bruno Costa", "idade": 34, "compras": [350.00, 500.00], "categoria": "Premium"},
    "45678912344": {"nome": "Carla Souza", "idade": 22, "compras": [50.00], "categoria": "Regular"},
    "78912345655": {"nome": "Diego Lima", "idade": 41, "compras": [15.00, 30.00, 25.50, 40.00], "categoria": "Regular"}
    }

def listar_clientes() :
      if not clientes:
            print("Nenhum cliente cadastrado ainda.")

      for cpf, dados in clientes.itens():
            print(f"CPF: {cpf}")
            print(f"Nome: {dados['nome']}")
            print(f"Idade: {dados['idade']}")
            print(f"Compras: {sum(dados['compras'])}")
      return

def cadastrar_cliente():
      cpf = input("Digite o CPF a ser cadastrado: ")
      novo_cliente = {}
      novo_cliente["nome"] = input("Digite o nome do cliente: ")
      novo_cliente["idade"] = input("Digite a idade do cliente: ")
      novo_cliente["compras"] = []
      novo_cliente["categoria"] = "Regular"

      clientes[cpf] = novo_cliente

def atualizar_cliente():
      pass
      
def excluir_cliente() :
      pass
      
def calcular_faturamento():
      pass
      
def fazer_compra():
      pass
      
def verificar_status():
      pass

def buscar_cliente():
    cpf = input("\nDigite o cpf do cliente: ")

    if cpf in clientes:      

      print(f"""
      Nome: {clientes[cpf]["nome"]} 
      Idade: {clientes[cpf]["idade"]}
      Total Compras: R${sum(clientes[cpf]["compras"]):.2f}
      Categoria: {clientes[cpf]["categoria"]}""")
        
    else:
        print("CPF não cadastrado.")

def exibir_menu():
      print("""\n====== MENU ======\n
O que deseja fazer?\n

1. Listar
2. Cadastrar
3. Atualizar
4. Excluir
5. Calcular faturamento
6. Fazer compra
7. Verificar status""")
        
      opcao = (input("\nEscolha a opção: "))

      if opcao == '1':
            listar_clientes()
            
      elif opcao == '2':
            cadastrar_cliente()

      elif opcao == '3': 
            atualizar_cliente()

      elif opcao == '4':
            excluir_cliente() 

      elif opcao == '5':
            calcular_faturamento() 

      elif opcao == '6':
            fazer_compra() 

      elif opcao == '7':
            verificar_status() 

      else:
            print("Opção inválida!") 

while True:
      exibir_menu()


