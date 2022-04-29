#!/usr/bin/env python3


# Refaça o exercício 35 dos triângulos acrescentando
#  o recurso de mostrar que tipo de triângulo
#  será formado
#
# EQUILÁTERO: todos os lados iguais
# ISÓCELES: dois lados iguais
# ESCALENO: todos os lados diferentes #

print('-=' * 15)
print('Analisador de Triângulos')
print('-=' * 15)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
A = bool(a < b + c)
B = bool(b < a + c)
C = bool(c < a + b)
print('A = ', A)
print('B = ', B)
print('C = ', C)
#   if (A == True and B == True and C == True):
if A is True and B is True and C is True:
    print('triangulo existe')
else:
    print('triangulo não existe')
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')
if a != b and a != c and b != c:
    print('Escaleno')
    print(a)
    print(b)
    print(c)
elif a == b and a == b and b == c:
    print('Equilátero')
    print(a)
    print(b)
    print(c)
else:
    print('Isóceles')
    print(a)
    print(b)
    print(c)
