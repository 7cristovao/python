''' Crie um programa que leia nome e duas
    notas de vários alunos e guarde tudo 
    em uma lista composta. No final, 
    mostre um boletim contendo a média de
    cada um e permita que o usuário possa
    mostrar as notas de cada aluno
    individualmente. '''
import math

alunos = []
respostaAluno = 0
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()
    if resposta in 'SsNn':
        if resposta == 'N':
            break
        else:
            continue
    else:
        while resposta not in 'SsNn':
            resposta = str(input('Quer continuar? [S/N] ')).upper().strip()
            if resposta == 'N':
                break
            else:
                continue
print('-' * 30)
print('No.   Nome           Média')
for c in range(0, len(alunos)):
    print(f' {c}    {alunos[c][0]}              {alunos[c][2]}')
while True:
    resposta = int(input('\nEscolha um aluno pelo número para mostrar as notas, digite 999 para sair: '))
    if resposta == 999:
        break
    else:
        c = resposta
        print(f'\nAs notas de {alunos[c][0]} são {alunos[c][1]}')
        break
print('\nFim do programa!')

