def contar_letra_no_arquivo():
    nome_arquivo = input("\nDigite o nome do arquivo de texto: ")
    total_letras = 0

    try:
        with open (f'Arquivos/{nome_arquivo}.txt', 'r', encoding = 'utf-8') as arquivo:
            letra_a_contar = input("Digite a letra a ser contada: ")  
            conteudo = arquivo.read().lower()            

            for caractere in conteudo:
                if caractere == letra_a_contar:
                    total_letras += 1
        
        if total_letras > 1:
            print(f"\nO arquivo possui {total_letras} letras '{letra_a_contar}'.\n")

        else:
            print(f"\nO arquivo possui {total_letras} letra '{letra_a_contar}'.\n")

    except FileNotFoundError:
        print("\nErro: O arquivo não foi encontrado. Verifique o nome.")

while True:
    contar_letra_no_arquivo()