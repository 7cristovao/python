#!/usr/bin/env python3


# Desenvolva um programa que leia SEIS NÚMEROS INTEIROS e
# mostre a soma apenas daqueles que forem PARES.
# 
# Se o valor digitado for ÍMPAR, desconsidere-o#

s = 0
for n in range(0, 6):
    n = int(input())
    if n % 2 == 1:
        del n
    else:
        s = s + n
print('soma = {} .'.format(s))
