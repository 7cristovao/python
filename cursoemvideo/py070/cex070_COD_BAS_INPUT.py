#!/usr/bin/env python3

# Crie um programa que lê o NOME e o PREÇO de 
# VÁRIOS PRODUTOS. O programa deverá perguntar 
# se o USUÁRIO vai continuar. No final mostre:
# 
# (A) Qual é o TOTAL GASTO na compra
# (B) Quantos produtos custam MAIS de R$ 1000
# (C) Qual é o NOME  do produto mais BARATO #

while True:
    nome = str(input('Nome prod.: ')).strip().upper()
    preco = int(input('Preço prod.: '))
    continua = ' '

    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break
print('fim')
