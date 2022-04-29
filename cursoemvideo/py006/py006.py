#!/usr/bin/env python3


# Crie um algoritmo que lê um número e mostre seu dobro, triplo
# e raiz quadrada #

import decimal

n = int(input('Digite um número: '))
dobro = 2 * n
print('O dobro de {} vale {}'.format(n, dobro))
triplo = 3 * n
print('O triplo de {} vale {}'.format(n, triplo))
raizQuadrada = (n ** (1/2))
print('A raiz quadrada de {} é igual a {}'.format(n, raizQuadrada))
