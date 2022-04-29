#!usr/bin/env python3


# Crie um programa que vai gerar CINCO NUMEROS ALEATORIOS
# e colocar um uma TUPLA.

# Depois disso, mostre a LISTAGEM DE NUMEROS gerados e tambem 
# indique o MENOR e o MAIOR  valor que estao na tupla.

from random import randint
n = 0
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: '.format(n, end=''))
for n in numeros:
    print('{} '.format(n, end=''))
print('O maior valor foi {}'.format(max(numeros)))
print('O menor valor foi {}'.format(min(numeros)))
