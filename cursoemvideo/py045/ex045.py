#!/usr/bin/env python3
# encoding: utf-8

# Crie um programa que faça o computador jogar jo-ken-pô com você

import random
S = "-+" * 27
print("{0:>25}\nJÓ-KEN-PÔ\n{0:>25}".format(S))
ó = str(input('Qual opção?\n UM p/PEDRA\n DOIS p/TESOURA \n TRÊS p/PAPEL\n'))
if ó == '1':
    print('Você pôs PEDRA')
elif ó == '2':
    print('Você pôs TESOURA')
elif ó == '3':
    print('Você pôs PAPEL')
elif ó != '1' or ó != '2' or ó != '3':
    print('Não vale!')
else:
    print('Não vale!')
# cs : computador sorteia
x = ('1', '2', '3')
cs = random.choice(x)
# print('O computador sorteou {}'.format(cs))
if cs == '1':
    print('O computador pôs PEDRA')
elif cs == '2':
    print('O computador pôs TESOURA')
elif cs == '3':
    print('O computador pôs PAPEL')
else:
    print('Não vale!')
if ó == cs:
    print('\nEmpatou!')
elif ó == '1' and cs == '2':
    print('\nVocê ganhou!')
elif ó == '1' and cs == '3':
    print('\nVocê perdeu!')
elif ó == '2' and cs == '1':
    print('\nVocê perdeu!')
elif ó == '2' and cs == '3':
    print('\nVocê ganhou!')
elif ó == '3' and cs == '1':
    print('\nVocê ganhou!')
elif ó == '3' and cs == '2':
    print('\nVocê perdeu!')

# pedra > tesoura
# tesoura > papel
# papel > pedra
