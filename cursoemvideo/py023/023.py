#!/usr/bin/env python3


# Desenvolva um código que lê um número de 0 a 9999 
# e mostre na tela cada um dos dígitos separados

n = str(input('Informe um número: '))
print('Analisando o número {}'.format(n))
print('algarismos = ', len(n))
algarismos = len(n)
if (algarismos == 1):
    print('unidade =', n)
elif (algarismos == 2):
    print('dezena =', n[0])
elif (algarismos == 3):
    print('centena =', n[0])
elif (algarismos == 4):
    print('milhar = ', n[0:1])
elif (algarismos == 5):
    print('milhar = ', n[0:2])
elif (algarismos == 6):
    print('milhar = ', n[0:3])
elif (algarismos == 7):
    print('milhar = ', n[0:4])
else:
    print('milhar = ', n[0:(algarismos-3)])
