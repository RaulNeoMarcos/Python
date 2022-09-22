from multiprocessing.sharedctypes import RawValue


nome = 'Raul'
idade = 37
altura = 1.80
estudando = True

print(nome)
print(idade)
print(altura)
print(estudando)

print(type(nome))
print(type(idade))
print(type(altura))
print(type(estudando))

nome = input('Qual seu nome?')

print('Seja bem vindo', nome)