clientes = {
    "12345678901": {"nome": "Ana Silva", "idade": 28, "compras": [120.50, 89.90, 45.00], "categoria": "VIP"},
    "98765432100": {"nome": "Bruno Costa", "idade": 34, "compras": [350.00, 500.00], "categoria": "Premium"},
    "45678912344": {"nome": "Carla Souza", "idade": 22, "compras": [50.00], "categoria": "Regular"},
    "78912345655": {"nome": "Diego Lima", "idade": 41, "compras": [15.00, 30.00, 25.50, 40.00], "categoria": "Regular"}
    }

def listar_clientes() :
      if not clientes:
            print("Nenhum cliente cadastrado ainda.")

      for cpf, dados in clientes.items():
            print(f"\nCPF: {cpf} | Nome: {dados['nome']} | Idade: {dados['idade']} | Compras: R$ {sum(dados['compras']):.2f} | Categoria: {dados['categoria']}")

def cadastrar_cliente():
      cpf = input("Digite o CPF a ser cadastrado: ")
      novo_cliente = {}
      novo_cliente["nome"] = input("Digite o nome do cliente: ")
      novo_cliente["idade"] = input("Digite a idade do cliente: ")
      novo_cliente["compras"] = []
      novo_cliente["categoria"] = "Regular"

      clientes[cpf] = novo_cliente

def exibir_cliente_parcial(cpf):
      print(f"\nNome: {clientes[cpf]['nome']}")
      print(f"Idade: {clientes[cpf]['idade']}")

def exibir_cliente_completo(cpf):

      print(f"""
            Nome: {clientes[cpf]["nome"]} 
            Idade: {clientes[cpf]["idade"]}
            Total Compras: R${sum(clientes[cpf]["compras"]):.2f}
            Categoria: {clientes[cpf]["categoria"]}""")

def buscar_cliente():
    cpf = input("\nDigite o CPF do cliente a ser encontrado: ")

    if cpf in clientes:      

      exibir_cliente_completo(cpf)
        
    else:
        print("CPF não cadastrado!")


def atualizar_cliente():

      while True:

            cpf = input("\nDigite o CPF do cliente a ser atualizado (0 para voltar): ")

            if cpf in clientes:

                  exibir_cliente_parcial(cpf)

                  print("""\nO que deseja atualizar?\n
      1. Nome
      2. Idade""")

                  opcao = input("\nDigite a opção: ")

                  if opcao == '1':
                        clientes[cpf]['nome'] = input("\nDigite o nome: ")
                        print("\nNome atualizado!")
                        exibir_cliente_parcial(cpf)

                  elif opcao == '2':
                        clientes[cpf]['idade'] = input("\nDigite a idade: ")
                        print("\nIdade atualizada!")
                        exibir_cliente_parcial(cpf)
                  else:
                        print("Opção inválida!")

            elif cpf == '0':
                  break

            else:
                  print("\nCPF não cadastrado!")      
      
def excluir_cliente() :

      while True:

            cpf = input("\nDigite o CPF do cliente a ser deletado (0 para voltar): ")

            if cpf in clientes:
                  del clientes[cpf]
                  print("\nCliente deletado!")

            elif cpf == '0':
                  break

            else:
                  print("\nCPF não cadastrado!")      

      
def calcular_faturamento_cliente():

      while True:

            cpf = input("\nDigite o CPF do cliente a calcular o faturamento (0 para voltar): ")

            if cpf in clientes:
                  print(f"\nO faturamento de {clientes[cpf]['nome']} é R$ {sum(clientes[cpf]['compras']):.2f}.")

            elif cpf == '0':
                  break

            else:
                  print("\nCPF não cadastrado!")          
      
def fazer_compra():

      while True:

            cpf = input("\nDigite o CPF do cliente a fazer compra (0 para voltar): ")

            if cpf in clientes:
                  print(f"\nNome: {clientes[cpf]['nome']} | Compras: R$ {sum(clientes[cpf]['compras']):.2f}")

                  valor_compra = float(input("\nDigite o novo valor da compra do cliente: "))
                  clientes[cpf]['compras'].append(valor_compra)
                  print("\nValor da compra atualizado!")
                  atualizar_categoria_cliente(cpf)
                  print(f"\nNome: {clientes[cpf]['nome']} | Compras: R$ {sum(clientes[cpf]['compras']):.2f}")

            elif cpf == '0':
                  break

            else:
                  print("\nCPF não cadastrado!")          
      
def atualizar_categoria_cliente(cpf):

      if sum(clientes[cpf]['compras']) >= 100:
            clientes[cpf]['categoria'] = "Vip"

def exibir_menu():
      print("""\n====== MENU ======\n
O que deseja fazer?\n
1. Listar
2. Cadastrar
3. Buscar
4. Atualizar
5. Excluir
6. Calcular faturamento
7. Fazer compra""")
        
      opcao = (input("\nEscolha a opção: "))

      if opcao == '1':
            listar_clientes()
            
      elif opcao == '2':
            cadastrar_cliente()

      elif opcao == '3':
            buscar_cliente()            

      elif opcao == '4': 
            atualizar_cliente()

      elif opcao == '5':
            excluir_cliente() 

      elif opcao == '6':
            calcular_faturamento_cliente() 

      elif opcao == '7':
            fazer_compra() 

      else:
            print("Opção inválida!") 

while True:
      exibir_menu()


