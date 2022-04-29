#!/usr/bin/env python3


# Faça um código que lê uma frase pelo teclado e mostre: 
# (1) Quantas vezes aparece a letra A 
# (2) Em que posição ela aparece a primeira vez 
# (3) Em que posição ela aparece a última vez #

frase = str(input('Digite uma frase: ')).strip()
frase = frase.upper()
contaA = frase.count('A')
print('A letra A aparece {} vezes na frase.'.format(contaA))
print('A primeira letra A apareceu na posição {}'.format(1+frase.find('A')))
print('A última letra A apareceu na posição {}'.format(1+frase.rfind('A')))
