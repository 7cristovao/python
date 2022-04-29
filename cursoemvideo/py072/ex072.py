#!/usr/bin/env python3


# TUPLA
# Crie um programa que tenha uma TUPLA totalmente preenchida com uma
# contagem por extenso, de ZERO ate VINTE.

# Seu programa deverá ler um numero pelo teclado
# ENTRE ZERO E VINTE e mostra-lo por EXTENSO

# x : numero em algarismo
# e : numero por extenso

x = int(input('Digite um n. '))
e = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito',
'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
print(e[x])
