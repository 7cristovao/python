#!/usr/bin/env python3


# Faca um programa que le CINCO VALORES NUMERICOS e os guarde 
# numa LISTA.

# No final, mostre qual foi o MAIOR e o MENOR valor
# digitado  e as suas respectivas POSICOES  na lista.

lista = []
for i in range(0, 5):
     lista.append(int(input('Dig. o valor: ')))
print(lista)
maior = max(lista)
print(max(lista))
menor = min(lista)
print(min(lista))
print(lista.index(maior))
print(lista.index(menor))

