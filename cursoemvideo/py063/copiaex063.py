#!/usr/bin/env python3


# Escreva um programa que lê um NÚMERO N inteiro qualquer
#  e mostre na tela os N primeiros elementos de uma 
# SEQUENCIA DE FIBONACCI.   

n = int(input('Digite n: '))
i = -1
while i < n:
    i = i + 1 
print((((1+(5**(1/2)))/2) ** i)-(((1+(5**(1/2)))/2) ** i) / (5 ** (1 / 2)))
print('fim')


