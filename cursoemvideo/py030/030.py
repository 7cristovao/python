#!/usr/bin/env python3


# Crie um programa que lê um número inteiro e mostre na tela se ele 
# é PAR ou ÍMPAR

x = int(input('Me diga um número qualquer: '))
type(x)
x % 2
if (x % 2) == 0:
    print('O número {} é PAR'.format(x))
elif (x % 2) == 1:
    print('O número {} é ÍMPAR'.format(x))
else:
    print('Não é um número inteiro')