#!/usr/bin/env python3


# Escreva um algoritmo que lê o comprimento do cateto oposto 
# e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa

# h : hipotenusa
# co : cateto oposto
# ca : cateto adjacente
from math import sqrt
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = sqrt((co ** 2) + (ca ** 2))
print('A hipotenusa vai medir {}'.format(h))