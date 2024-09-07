''' Faça um programa que tenha uma lista chamada
    números e duas funções chamadas sorteia() e 
    somaPar(). A primeira função vai sortear 5
    números e vai colocá-los dentro da lista e 
    a segunda função vai mostrar a soma entre
    todos os valores PARES sorteados pela função
    anterior. '''

from random import randint

numeros = []

def sorteia(num1, num2, num3, num4, num5):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        numeros.append(randint(0, 10))
    for c in numeros:
        print(f'{c}', end=' ')
    print('PRONTO!')

def somaPar():
    print(f'Somando os valores pares de {numeros}, temos ', end=' ')
    s = 0
    for c in numeros:
        if c % 2 == 0:
            s = s + c
            print(c, end=' ')
    print('\n')


sorteia(1,1,1,1,1)
somaPar()