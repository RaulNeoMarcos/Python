# Criando

dicionario = {}
dicionario = dict()

dicionario = {'nome': 'Raul', 'idade': 26, 'altura': 1.77}

print(dicionario)
print(dicionario['idade'])

# add elementos

dicionario['programdor'] = True
print(dicionario)

dicionario['altura'] = 2
print(dicionario)

# percorrendo o dicionario
for chave in dicionario:
    print(chave, dicionario[chave])

# Verificando existencia da chave no dicionario 
print('peso' in dicionario)
print('altura' in dicionario)