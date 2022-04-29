#!/usr/bin/env python3


# Desenvolva um programa que leia SEIS NÚMEROS INTEIROS e
# mostre a soma apenas daqueles que forem PARES.
# 
# Se o valor digitado for ÍMPAR, desconsidere-o#

soma = 0
cont = 0
for c in range(0, 6):
    num = int(input('Digite o {} valor: '.format(cont)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} números pares e a soma foi {}'.format(cont, soma))
