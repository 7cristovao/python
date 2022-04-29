#!/usr/bin/env python3


# Faça um código que lê o nome completo de uma pessoa
# e mostre em seguida o primeiro e o último nome de forma separada

nome = str(input('Digite seu nome completo: '))
lista = nome.split()
print(lista)
rlista = nome.rsplit()
irlista = rlista[::-1]
print(irlista)
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(lista[0]))
print('Seu último nome é {}'.format(irlista[0]))

