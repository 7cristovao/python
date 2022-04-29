#!/usr/bin/env python3


# Escreva um algoritmo que lê quanto dinheiro uma pessoa
# tem na carteira e mostre quantos dólares ela pode comprar

BRL = float(input('Quanto dinheiro você tem na carteira? R$ '))
USD = 1.01 * BRL
print('Com R$ {:.2f} você pode comprar US$ {:.2f}'.format(BRL, USD))