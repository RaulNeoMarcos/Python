numero_sorteado = 15

numero_escolhido = int(input('Digite um numero:'))

"""
if numero_sorteado == numero_escolhido:
    print('acertou')
else:
    print('errou')
"""

while numero_escolhido != numero_sorteado:
    print('Errou')
    numero_escolhido = int(input('Digite um numero:'))

print('Parabens acertou miseravel')

# EXEMPLO 2

contador = 0

while contador < 5:
    print(contador)
    contador += 1
