idade = int(input('Qual sua idade?'))

if idade >= 18:
    print('Já pode beber')
else:
    print('Beba leite')   

media = float(input('Qual sua média em matematica?'))    
presenca = 50

if media >= 7 and presenca >= 70:
    print('Passou de ano')
elif media >= 5 and presenca >= 70:
    print('Ficou em recuperação')
else:
    print('Você foi reprovado')    