#!/usr/bin/env python3


# Escreva um programa que lê um NÚMERO N inteiro qualquer
#  e mostre na tela os N primeiros elementos de uma 
# SEQUENCIA DE FIBONACCI.   

from math import sqrt, trunc
n = int(input('Digite n: '))
i = 0
for i in range(1, n):
     i = i + 1 
     print(trunc((pow((1+sqrt(5))/2,i) - pow((1-sqrt(5))/2,i)) / sqrt(5)))
     #print( (((((5**(1/2))+1)/2) ** i)-((((5**(1/2))-1)/2) ** i))/ (5**(1/2)) )
print('fim')


