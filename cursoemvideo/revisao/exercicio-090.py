''' Faça um programa que leia nome e média de um
    aluno, guardando também a situação em um
    dicionário. No final, mostre o conteúdo da
    estrutura na tela. '''

nome = str(input('Nome: '))
media = float(input(f'Média de {nome}: '))
aluno = dict()
aluno = {'nome': nome, 'média': media}

print(f'Nome é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["média"]}')
if aluno['média'] >= 6:
    status = 'Aprovado'
else:
    status = 'Reprovado'
print(f'Situação é igual a {status}')