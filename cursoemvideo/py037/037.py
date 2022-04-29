#!/usr/bin/env python


# Escreva um programa que leia um número inteiro qualquer e
# peça para o usuário escolher qual será a BASE DE CONVERSÃO:
#
# 1 para binário
# 2 para octal
# 3 para hexadecimal #

x = int(input('Digite um número inteiro: '))
print('\n Escolha a base de conversão:\n1 p/ bin\n2 p/ oct\n3 p/ hex')
b = int(input('A base escolhida é a '))
# b : base de conversão escolhida
if b == 1:
    print('Em binário seu número é {}'.format(bin(x)))
elif b == 2:
    print('Em octal seu número é {}'.format(oct(x)))
else:
    print('Em hexadecimal seu número é {}'.format(hex(x)))
