#!/usr/bin/env python3


# TUPLA
# Crie um programa que tenha uma TUPLA totalmente preenchida com uma
# contagem por extenso, de ZERO ate VINTE.

# Seu programa deverá ler um numero pelo teclado
# ENTRE ZERO E VINTE e mostra-lo por EXTENSO

# x : numero em algarismo
# e : numero por extenso

count = 0
while True:
    x = int(input('Digite um numero: '))
    if x >= 0 and x < 21:
        e = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete',
'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
        print(e[x])
        break
    else:
        print('Digite um numero entre 0 e 20: ')
        False
print('fim')
