#!usr/bin/env python3
#encoding: utf-8

# Crie um programa que vai ler VARIOS NUMEROS  e colocar em uma LISTA

# Depois disso crie DUAS LISTAS EXTRAS que vao
# conter apenas os valores  PARES e os valores IMPARES digitados,
# respectivamente.

# Ao final, mostre o conteudo das TRES LISTAS geradas.

l = []
while 999 not in l:
	l.append(int(input(l)))
l.pop()
print(l)
print('fim')

if l[0] % 2 == 0:
	lpar = l
	print('pares = {}'.format(lpar))
else:
	limpar = l[0]
	print('impares = {}'.format(limpar))

