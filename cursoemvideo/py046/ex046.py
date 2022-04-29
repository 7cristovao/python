#!/usr/bin/env python3


# Faça um programa que mostre na tela uma CONTAGEM REGRESSIVA
# para o estouro de fogos de artifício, indo de
# DEZ ATÉ ZERO,  com uma pausa de SEGUNDO  entre eles.

from time import sleep

C = 0
for C in range(10, 0, -1):
    print(C)
    sleep(1)
print('fda')
