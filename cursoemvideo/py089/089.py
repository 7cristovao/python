#!/usr/bin/env python3


# Crie um programa que le NOME e DUAS NOTAS de varios alunos
# e guarde tudo em uma LISTA COMPOSTA. No final, mostra um
# BOLETIM contendo a MEDIA de cada um e permita que o usuario 
# possa mostrar as NOTAS de cada aluno individualmente

# OBS: TRES niveis de lista

ficha = list()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? (S/N) '))
    if resp in 'Nn':
        break
print(ficha)
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')