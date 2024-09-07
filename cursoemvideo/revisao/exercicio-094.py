''' Crie um programa que leia nome, sexo e 
    idade de várias pessoas, guardando os 
    dados de cada pessoa em um dicionário
    e todos os dicionários em uma lista. 
    No final, mostre:
    
    A) Quantas pessoas foram cadastradas
    B) A média de idade do grupo.
    C) Uma lista com todas as mulheres.
    D) Uma lista com todas as pessoas
    com idade acima da média. '''

pessoas = dict()
grupo = list()
soma = media = 0
while True:
    nome = str(input('Nome: '))
    pessoas['nome'] = nome
    sexo = str(input('Sexo: ')).upper().strip()
    while sexo not in 'MmFf':
        sexo = str(input('Sexo: ')).upper().strip() 
    pessoas['sexo'] = sexo
    idade = int(input('Idade: '))
    pessoas['idade'] = idade
    soma = soma + pessoas['idade']
    grupo.append(pessoas.copy())
    resposta = str(input('Quer continuar? [S/N]')).upper().strip()
    while resposta not in 'SsNn':
        resposta = str(input('Quer continuar? [S/N]')).upper().strip()
    if resposta in 'Nn':
        break
    else:
        continue
quantidade = len(grupo)
print(f'- O grupo tem {quantidade} pessoas.')
media = soma / quantidade
print(f'- A média das idades é de {media:5.2f} anos.')
print(f'- As mulheres cadastradas foram ', end='')
for p in grupo:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print(f'- Lista das pessoas que estão acima da média: ')
for p in grupo:
    if p['idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('\n<< ENCERRADO >>')