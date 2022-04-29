#!/usr/bin/env python3


# Lê tres segmentos de reta e diz se o triângulo existe ou não


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
if (A == True and B == True and C == True):
    print('triangulo existe')
else:
    print('triangulo não existe')
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')


#      ^      
# b  /   \ c
#   -------   
#     a