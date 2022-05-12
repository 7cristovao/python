#!/usr/bin/env python3


# Crie um programa onde o usuario possa digitar varios 
# VALORES NUMERICOS e cadastre-os um uma LISTA.
# Caso o numero ja exista la dentro ela 
# NAO SERA ADICIONADA. 
# No final serao exibidos todos os VALORES UNICOS digitados, em 
# ORDEM CRESCENTE.
# p : posicao
# r : resposta

numeros = list()   # (1) 
while True:   # (1) 
    n = int(input('Dig. o valor: '))   # (1) 
    if n not in numeros:  # (2) (3)
        numeros.append(n)  # (2) (3)
        print('valor adicionado com sucesso')  # (2) (3) 
    else:  # (2)  (3) 
        print('valor duplicado, nao vai ser adicionado') # (2) (3) 
    r = str(input('Quer continuar? [S/N] '))   # (1) 
    if r in 'Nn':   # (1) 
        break   # (1) 
numeros.sort()
print('Voce digitou os valores {}'.format(numeros))
# (1)  lista comeca vazia, para varios numeros usa enquanto com break
# (2)  vai inserir se numero nao estiver na lista
# (3)  em outras linguagens de programacao eh necessario inserir um loop aqui
