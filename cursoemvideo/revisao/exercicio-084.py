''' Faça um programa que leia
    nome e peso de várias pessoas, 
    guardando tudo em uma lista.
    No final, mostre:
    
    A) Quantas pessoas foram cadastradas. 
    
    B) Uma listagem com as pessoas mais
    pesadas.
    
    C) Uma listagem com as pessoas mais 
    leves. '''

pessoas = []
dado = []
while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    if len(pessoas) == 0:
        maisPesada = maisLeve = dado[1]
    else:
        if dado[1] > maisPesada:
            maisPesada = dado[1]
        if dado[1] < maisLeve:
            maisLeve = dado[1]
    pessoas.append(dado[:])
    dado.clear()
    resposta = str(input('Quer continuar? '))
    if resposta in 'Nn':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'A lista das pessoas é {pessoas}')
print(f'Mais pesada(s) = {maisPesada}')
print(f'Mais leve(s) = {maisLeve}')
print('FIM')
