#!/usr/bin/env python3


# Faça um programa que leia um NÚMERO qualquer
# e mostre seu FATORIAL.

# Ex:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

# j : contador
# x : uma variável inteira qualquer 
# f : fatorial

j = 0
x = 0
f = 0
x = int(input('x = '))
f = 1
while j in range(1, x + 1):
    f *= j
print('fatorial = {}'.format(f))
