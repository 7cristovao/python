#!/usr/bin/env python3


# Crie um programa que sorteie a ordem de 
# apresentação de quatro alunos de um seminário
# Mostre a ordem sorteada

from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('As colocacoes foram sorteadas assim')
print(lista)