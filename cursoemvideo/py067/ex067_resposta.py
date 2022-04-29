#!/usr/bin/env python

# Faça um programa que mostre a TABUADA de VÁRIOS NÚMEROS, 
# um de cada vez, para cada valor digitado pelo usuário
# O programa seá INTERROMPIDO quando o número solicitado
# for NEGATIVO #

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    for c in range(1, 11):
        print('{} x {} = {}'.format(n, c, n * c))
print('Programa tabuada encerrado. Volte sempre!')
