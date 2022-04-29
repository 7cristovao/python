#!/usr/bin/env python3

import string
from random import shuffle, choice
x = input('Que número eu pensei? ')
lista = ['0', '1', '2', '3', '4', '5']
y = choice(lista)
print('PROCESSANDO...')
print(x)
try:
    x = int(x)
    if (x == 0 or x == 1 or x == 2 or x == 3 or x == 4 or x == 5):
       print(type(x))
       print('Igual a ZERO ou UM ou DOIS ou TRÊS ou QUATRO ou CINCO')
    elif (x == int(x)):
       print(type(x))
       print('Diferente de ZERO ou UM ou DOIS ou TRES ou QUATRO ou CINCO')
except ValueError as err:
    print('Digite um número entre ZERO e CINCO')
    #print(err)
 #GANHEI! Eu pensei no número {} e não no {}'.format(x,x))
 #PARABÉNS! Você conseguiu me vencer!')