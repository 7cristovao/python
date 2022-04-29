#!/usr/bin/env python3


# Faça um programa que leia um NÚMERO qualquer
# e mostre seu FATORIAL.

# Ex:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

# j : contador
# x : uma variável inteira qualquer 
# f : fatorial

n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))

