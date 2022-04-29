#!/usr/bin/env python3

# Faça um programa que jogue PAR OU IMPAR com o computador. 
# O jogo só será interrompido quando o jogador PERDER, 
# mostrando o total de vitórias consecutivas que ele conquistou
# no final do jogo.

# n : jogador
# o : computador

from random import randint
count = 0
while True:
    n = str(input('Digite P para par ou I para ímpar: ')).upper().strip()
    if n == 'P':
        n = 0
    elif n == 'I':
        n = 1
    else:
        print('Opção inválida')
    o = randint(0, 1)
    if n == 0:
        print('Você escolheu PAR')
    else:
        print('Você escolheu IMPAR')
    if o == 0:
        print('\nComputador escolheu PAR')
    else:
        print('\nComputador escolheu IMPAR')
    if n == o:
        print('\n\nVocê venceu!')
        count += 1
    else:
        print('\n\nComputador venceu!')
        break
print('Computador venceu! Fim de jogo!')
print('Você venceu {}!'.format(count))
