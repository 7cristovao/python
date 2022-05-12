#!/usr/bin/env python3


# Crie um programa que le NOME e DUAS NOTAS de varios alunos
# e guarde tudo em uma LISTA COMPOSTA. No final, mostra um
# BOLETIM contendo a MEDIA de cada um e permita que o usuario 
# possa mostrar as NOTAS de cada aluno individualmente

# OBS: TRES niveis de lista

nome = []
p1 = []
p2 = []
lista = [nome, p1, p2]
while True:
    nome.append(str(input('Nome: ')))
    p1.append(float(input('Nota 1: ')))
    p2.append(float(input('Nota 2: ')))
    resp = input('Outro aluno? (S/N): ')

    if resp in 'Nn':
        break
print(lista)

#somatoria é (s = s + i)
#media é ((s = s + i)/i)
print('BOLETIM')
print(lista[0][0])
print(lista[1][0])
print(lista[2][0])
'''
print('BOLETIM')
print(lista[0][1])
print(lista[1][1])
print(lista[2][1])
'''
i = 0
for i in range(0,len(lista)):
    print(lista[i])
    print('m = ', )