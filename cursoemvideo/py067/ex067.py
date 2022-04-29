#!/usr/bin/env python3

# Faça um programa que mostre a TABUADA de VÁRIOS NÚMEROS, 
# um de cada vez, para cada valor digitado pelo usuário
# O programa será INTERROMPIDO quando o número solicitado
# for NEGATIVO #

# f : fator
# n : número fator

from time import sleep
f = 0
n = int(input('Tabuada do '))
while True:
    while True:
        f += 1
        print(' {} x  {} =   {}'.format(n, f, n * f))
        if f >= 10:
            sleep(1)
            f = 0            
            n = int(input('Tabuada do ')) 
        elif n < 0:
            break
    break
print('fim')
