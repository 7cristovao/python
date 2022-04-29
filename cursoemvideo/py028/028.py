#!/usr/bin/env python3


# Escreva um programa que faça o computador "pensar" em um número inteiro entre
# ZERO  e CINCO  e peça para o usuário tentar descobrir qual foi o 
# número escolhido pelo conmputador.
# 
# O programa deverá escrever na tela se o usuário venceu ou perdeu #

import string
from random import shuffle, choice
x = input('Que número eu pensei? ')
lista = ['0', '1', '2', '3', '4', '5']
y = choice(lista)
print('y = ', y)
print(type(y))
y = int(y)
print(type(y))
print('PROCESSANDO...')
print('x = ', x)
try:
   x = int(x)
   if (x == 0 or x == 1 or x == 2 or x == 3 or x == 4 or x == 5):
      print(type(x))
      print('Igual a ZERO ou UM ou DOIS ou TRÊS ou QUATRO ou CINCO')
      if (int(x) == int(y)):
         print('PARABÉNS! Você conseguiu me vencer!')
      else:
         print('GANHEI! Eu pensei no número {} e não no {}'.format(y, x))
   elif (x == int(x)):
      print(type(x))
      print('Diferente de ZERO ou UM ou DOIS ou TRES ou QUATRO ou CINCO')      
except ValueError as err:
   print('Digite um número entre ZERO e CINCO')
   #print(err)