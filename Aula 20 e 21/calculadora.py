
def menu():
    while True:
        print("""\n====== Calculadora ======\n
    1. Adição
    2. Subtração
    3. Multiplicação
    4. Divisão
    0. Sair""")
        
        operacao = int(input("\nEscolha a operação: "))
        n1 = int(input("Digite primeiro número: "))
        n2 = int(input("Digite segundo número: "))
    
        if operacao == 1:
            return adicao(n1, n2)        

        elif operacao == 2:
            return subtracao(n1, n2)

        elif operacao == 3:
            return multiplicacao(n1, n2)

        elif operacao == 4:
            return divisao(n1, n2)
        
        elif operacao == 0:
            print("FIM")
            break

        else:
            print("Opção inválida!")    

def adicao(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    return n1 / n2


print(menu())
