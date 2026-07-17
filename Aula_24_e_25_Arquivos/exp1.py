#Abrindo um arquivo para leitura
arquivo = open('Arquivos/exemplo3.txt', 'r', encoding="utf-8")
conteudo = arquivo.read()
print(conteudo)
arquivo.close

arquivo = open('Arquivos/exemplo3.txt', 'a', encoding="utf-8")
arquivo.write('\nElefante')
arquivo.close

arquivo = open('Arquivos/exemplo3.txt', 'r', encoding="utf-8")
conteudo = arquivo.read()
print(conteudo)
arquivo.close




