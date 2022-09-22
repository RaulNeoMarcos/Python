"""
Questão 2.
Crie um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual
dos seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se encontra. Caso o valor não
esteja em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”. Veja
alguns exemplo abaixo:

"""

entrada = int(input('Digite um valor de 0 até 100:'))

if entrada >= 0 and entrada <= 25:
    print('No intervalo [0,25]')
elif entrada >= 26 and entrada <= 50:
    print('No intervalo [25,50]')
elif entrada >= 51 and entrada <= 75:
    print('No intervalo [50,75]')
elif entrada >= 76 and entrada <= 100:
    print('No intervalo [75,100]')
else:
    print('Fora de intervalo')    