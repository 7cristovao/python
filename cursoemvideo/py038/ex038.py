#!/usr/bin/env python3


# Escreva um programa que lê dois números inteiros,
# compare-os mostrando na tela uma mensagem: #

# (1) O primeiro valor é MAIOR
# (2) O segundo valor é MAIOR
# (3) NÃO EXISTE valor maior, os dois são iguais

z = int(input('Digite um número inteiro: '))
Z = int(input('Digite outro número inteiro: '))
if z > Z:
    print(f'O primeiro valor {z} é maior que {Z}')
elif Z > z:
    print(f'O segundo valor {Z} é maior que {z}')
else:
    print('Não existe valor maior, os dois são iguais')
