#!/usr/bin/env python3

# Crie um programa que lê o NOME e o PREÇO de 
# VÁRIOS PRODUTOS. O programa deverá perguntar 
# se o USUÁRIO vai continuar. No final mostre:
# 
# (A) Qual é o TOTAL GASTO na compra
# (B) Quantos produtos custam MAIS de R$ 1000
# (C) Qual é o NOME  do produto mais BARATO #

soma_preco = 0
maior_que_1000 = 0 
menor_preco = 0
maior_preco = 0
while True:
    nome = str(input('Nome prod.: ')).strip().upper()
    preco = int(input('Preço prod.: '))
    soma_preco += preco
 
    if preco == 1:
#       maior_preco = preco
        menor_preco = preco
    else:
#        if preco > maior_preco:
#            maior_preco = preco
        if preco < menor_preco:
            menor_preco = preco
        else:                  
            menor_preco = preco
          

    if preco > 1000:
        maior_que_1000 += 1

    continua = ' '

    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break
     

print('gasto na compra = {}'.format(soma_preco))
print('maior que 1000 = {}'.format(maior_que_1000))
print('menor preço = {}'.format(menor_preco))
print('fim')
