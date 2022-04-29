#!/usr/bin/env python3


#  Faça um programa que leia o PESO de CINCO PESSOAS.
# No final, mostre qual foi o MAIOR e o MENOR peso.

#p = 0
menor_p = 0
maior_p = 0
for p in range(1, 6):
    p = int(input('Dig. o peso: '))
    if p == 1:
        menor_p = p
        maior_p = p
    else:
        if menor_p > p:
            menor_p = p
        if maior_p < p:
            maior_p = p
print(menor_p)
print(maior_p)
