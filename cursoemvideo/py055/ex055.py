#!/usr/bin/env python3


#  Faça um programa que leia o PESO de CINCO PESSOAS.
# No final, mostre qual foi o MAIOR e o MENOR peso.

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {} pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}kg'.format(maior))
print('O menor peso lido foi de {}kg'.format(menor))
