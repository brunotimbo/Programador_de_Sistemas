#Abrindo um arquivo para escrita
arquivo = open('Arquivos/exemplo2.txt', 'w', encoding="utf-8")
arquivo.write('Esta é uma nova linha de texto.\n')
arquivo.write('Adicionado outra linha')
arquivo.close