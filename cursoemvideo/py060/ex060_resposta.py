#!/usr/bin/env python3


# Faça um programa que leia um NÚMERO qualquer
# e mostre seu FATORIAL.

# Ex:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

# j : contador
# x : uma variável inteira qualquer 
# f : fatorial

from time import sleep
from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))

