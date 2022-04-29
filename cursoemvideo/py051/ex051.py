#!/usr/bin/env python3


# Desenvolva um programa que leia o PRIMEIRO TERMO
# e a RAZÃO de uma PROGRESSÃO ARITMÉTICA. 
# No final, mostre os DEZ primeiros termos dessa 
# progressão. 

# a_i : termo_índice
# a_0 : primeiro_termo
# r : razão
# i : índice

# a_i = a_0 + r * i
# a_0 = a_0 + r * 0
# a_1 = a_0 + r * 1
# a_2 = a_0 + r * 2
# a_3 = a_0 + r * 3
# a_4 = a_0 + r * 4
# a_5 = a_0 + r * 5
# a_6 = a_0 + r * 6
# a_7 = a_0 + r * 7
# a_8 = a_0 + r * 8
# a_9 = a_0 + r * 9

a_0 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
cont = 0
for i in range(0, 10):
     a_i = a_0 + r * i+1
     cont += 1
     print ('O {}º termo da PA é igual a {} '.format(cont, a_i-1))
print('fim\n')


