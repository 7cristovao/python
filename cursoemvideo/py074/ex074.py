#!/usr/bin/env python3


# Crie um programa que vai gerar CINCO NUMEROS ALEATORIOS
# e colocar um uma TUPLA.

# Depois disso, mostre a LISTAGEM DE NUMEROS gerados e tambem 
# indique o MENOR e o MAIOR  valor que estao na tupla.

from random import random

numeros = (random(), random(), random(), random(), random())
menor_num = 1
maior_num = 0 
# num = 0  # Pega essa! Se usar essa variavel valores iguais ficam zeradas
print(numeros)
for num in numeros:
    numeros
    if num == 1: 
        menor_num = num
        maior_num = num
    else:
        if num > maior_num:
            maior_num = num
        if num < menor_num:
            menor_num = num
print(menor_num)
print(maior_num)
