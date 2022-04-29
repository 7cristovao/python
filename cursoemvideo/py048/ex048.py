#!/usr/bin/env python3


# Faça um algoritmo que calcule a SOMA entre todos
# os NÚMEROS IMPARES que são MÚLTIPLOS DE TRÊS e
# que se encontram no intervalo de
# UM ATÉ 500            

s = 0
for n in range(3, 501, 6):
    s += n
print(f'a soma é igual a {s}')
print('\n')

# conceito de contador   c = c + 1
# contagem de 1 até 500
#                   ... de números ímpares
#                   ... divisível por 3
# conceito de acumulador s = s + c
