#!/usr/bin/env python3


# Crie um programa que lê um ângulo qualquer e mostre seu 
# seno, cosseno e tangente #

# a : angulo em graus
from math import sin, cos, tan, radians
a = float(input('Digite o ângulo que você deseja: '))
print('O ângulo de {} tem o SENO de {:.2f}'.format(a,sin(radians(a))))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(a,cos(radians(a))))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(a,tan(radians(a))))