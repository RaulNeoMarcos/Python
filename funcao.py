from typing import NoReturn


def saudacao(nome, curso):
    print(f'Seja bem-vindo(a), {nome}!')
    print(
        f'Olá, é um prazer conhece-lo, que bom está fazendo o curso de {curso}')


saudacao('Raul', 'Python')


# função com parametro default

def saudacaoDefault(nome, curso='C#'):
    print(f'Seja bem-vindo(a), {nome}!')
    print(
        f'Olá, é um prazer conhece-lo, que bom está fazendo o curso de {curso}')


saudacaoDefault('Raul')

# funcção com retorno


def soma(num1, num2):
    return num1 + num2


resultado = soma(5, 12)
print(resultado)


def calculadora(num1, num2, operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2

resultado = calculadora(2,2,'-')
print(resultado)