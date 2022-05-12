#!usr/bin/env python3
#encoding: utf-8

# Crie um programa que vai ler VARIOS NUMEROS e colocar numa LISTA
#
# Depois disso mostre:
# 
# A) QUANTOS numeros foram digitados.
#
#B) A lista de valores ordenada de forma DECRESCENTE.
#
# C) Se  o valor 5 foi digitado e esta ou nao na LISTA.

l = []
print(l)
while 999 not in l:
	l.append(int(input(l)))
print(l)
print('fim')
l.pop()
print('Foram digitados {} numeros'.format(len(l)))
l.sort()
print('\nEm ordem crescente fica {}'.format(l))
if 5 in l:
	print('\nO valor 5 está na lista')
else:
	print('\nO valor 5 não está na lista')
