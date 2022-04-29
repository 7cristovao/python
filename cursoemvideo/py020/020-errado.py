#!/usr/bin/env python3


from random import shuffle
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
n1 = str(n1)
n2 = str(n2)
n3 = str(n3)
n4 = str(n4)
lista = [n1, n2, n3, n4]
shuffle(lista)
print('As colocacoes foram sorteadas assim')
print(str.format(lista))