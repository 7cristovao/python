#!/usr/bin/env python3


# Crie um programa para ler o ANO DE NASCIMENTO de 
# SETE PESSOAS. No final mostre quantas pessoas 
# ainda não atingiram a maioridade e quantas já 
# são maiores.

# an : ano de nascimento
# AA : ano atual

# idade : idade atual

#  c : contador de inputs
# c1 : contador de menores de idade
# c2 : contador de maiores de idade

import datetime

c1 = 0
c2 = 0
for c in range(0, 7):
    an = input('Digite o ano de nascimento: ')
    AA = str(datetime.date.today())
    AA = AA[0:4]
    idade = int(AA) - int(an)
    print('idade da pessoa {} é de {} anos'.format(c,idade))
    if idade < 18:
        c1 += 1
        print(c1)
    elif idade >= 18:
        c2 += 1
        print(c2)
print('total de menores = {}'.format(c1))
print('total de maiores = {}'.format(c2))
