
"""
notas = [7.9, 9.7, 8.2]

print(notas[0])
print(notas[1])
print(notas[2])

"""

# Criando Listas
lista = []
lista = list()
lista = [26, 'Walisson', 3.14, False]

# imprimindo do começo para o final

# print(lista[0])
# print(lista[1])
# print(lista[2])
# print(lista[3])
# print(lista[4])

# imprimindo de tras para frente

# print(lista[-1])
# print(lista[-2])
# print(lista[-3])
# print(lista[-4])

# imprimindo com range

# print(lista[0:2])
# print(lista[1:3])
# print(lista[2:2])

for elemento in lista:
    print(elemento)

# tamando
print(len(lista))

# indice da lista
for i in range(len(lista)):
    print(i)

# valor no indice i da lista
for i in range(len(lista)):
    print(lista[i])


# Adicionar elemento no final da lista

lista.append(2)
print(lista)

# Adicionar elemento no indice e com valor informado

lista.insert(2, 'Raul')
print(lista)

# juntar 2 listas

lista2 = [1, 2, 3]
lista.extend(lista2)
print(lista)

# remover da lista

# tirou o ultimo
lista.pop()
print(lista)

# tirou do indice informado
lista.pop(0)
print(lista)

# remover o primeiro pelo valor que esta na lista

lista.remove('Raul')
print(lista)

# quantas x o elemento especifico aparece na lista

print(lista.count(2))

# Em qual indice o valor do elemento está

print(lista.index(3.14))

# ondenar a lista

lista3 = [1, 4, 6, 2, 7, 3, 10]
lista3.sort()
print(lista3)
lista3.sort(reverse=True)
print(lista3)

#Funções

#tamanho da lista
print(len(lista3))

#somar elemento da lista
print(sum(lista3))

#maior elemento
print(max(lista3))

#menor elemento
print(min(lista3))


