#!/usr/bin/env python3


# Crie um programa que le varios numeros inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a CONDIÇÃO DE PARADA. No final mostre QUANTOS NÚMEROS
# foram digitados e qual foi a SOMA entre eles
# (tire o flag) #

# n : numero
# q : quantidade
# s : soma

q = s = 0
n = int(input('Digite um numero, [999 para parar]: '))
while n != 999:
    q += 1 
    s += n 
    n = int(input('Digite um n.: '))
print('quant = {}'.format(q))
print('soma  = {}'.format(s))
print('fim')
