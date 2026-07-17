lista_frutas = ["maçã", "banana", "laranja", "uva", "pêra"]
dicionario_frutas = {"maçã": "Uma fruta vermelha.",
                     "banana": "Uma fruta amarela.",
                     "laranja": "Uma fruta laranja.",
                     "uva": "Uma fruta roxa.",
                     "pêra": "Uma fruta verde."}

print(lista_frutas[0])
print(dicionario_frutas["maçã"])

del dicionario_frutas['laranja']

print(dicionario_frutas["maçã"])

if 'banana' in dicionario_frutas:
    print('Sim')

else:
    print('Não')

for i in dicionario_frutas:
    print(dicionario_frutas[i])