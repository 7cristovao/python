#!/usr/bin/env python3

# Crie um programa que lê o NOME e o PREÇO de 
# VÁRIOS PRODUTOS. O programa deverá perguntar 
# se o USUÁRIO vai continuar. No final mostre:
# 
# (A) Qual é o TOTAL GASTO na compra
# (B) Quantos produtos custam MAIS de R$ 1000
# (C) Qual é o NOME  do produto mais BARATO #

total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco    
    if preco > 1000:
        totmil += 1
    if cont == 1:  # variante:    if cont == 1 or preco < menor:
        menor = preco         #       manter       
        barato = produto      #       manter
    else:                     #       n manter
        if preco < menor:     #       n manter
            menor = preco     #       n manter
            barato = produto  #       n manter
    resp = ' '
    while resp not in 'SN':
         resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
         break

print('O total da compra foi {:10.2f}'.format(total))
print('Temos {} produtos custando mais de R$ 1000.00'.format(totmil))
print('O produto mais barato custa R$ {:.2f}')
print('O produto mais barato foi {} que custa R${:.2f}'.format(barato, menor))
