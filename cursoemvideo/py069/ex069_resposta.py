#!/usr/bin/env python3

# Crie um programa que lê a IDADE  e o SEXO  de 
# VÁRIAS PESSOAS. A cada pessoa cadastrada, o programa 
# deverá perguntar se o USUÁRIO  quer ou não continuar.
# No final mostre:

# (A) quantas pessoas tem mais de 18 ANOS
# (B) Quantos HOMENS foram cadastrados
# (C) Quantas MULHERES tem menos de 20 ANOS

tot18 = 0
totH = 0
totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('Total de pessoas com mais de 18 anos: {}'.format(tot18))
print('Ao todo temos {} homens cadastrados'.format(totH))
print('E temos {} mulheres com menos de 20 anos'.format(totM20))
