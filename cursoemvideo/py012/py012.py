#!/usr/bin/env python3

# Faça um programa que lê o preço de um produto e mostra seu novo preço
# com 5 % de desconto

preço = float(input('Qual é o preço do produto? R$'))
print('O produto que custava R$ {:.2f}, na promoção com desconto de {}% vai custar R${:.2f}'.format(preço, 5, preço * 0.95))
