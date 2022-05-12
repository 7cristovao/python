#!/usr/bin/env python3


# Faca um programa que le CINCO VALORES NUMERICOS e os guarde 
# numa LISTA.

# No final, mostre qual foi o MAIOR e o MENOR valor
# digitado  e as suas respectivas POSICOES  na lista.

listanum = []
mai = 0
men = 0
for c in range(0, 5):
     listanum.append(int(input('Dig. o valor para a posicao {} '.format(c))))
     if c == 0:
         mai = men = listanum[c]
     else:       
         if listanum[c] > mai:
             mai = listanum[c]
         if listanum[c] < men:
             men = listanum[c]
print()
print('Voce digitou os valores {}.'.format(listanum))
print('O maior valor digitado foi {} nas posicoes '.format(mai), end='')
for i, v in enumerate(listanum):
    if v == mai:
        print('{}... '.format(i), end='')
print()
print('O menor valor digitado foi {} nas posicoes '.format(men), end='') 
for i, v in enumerate(listanum):
    if v == men:
        print('{}... '.format(i), end='')
print()
