#!/usr/bin/env python3


# 58

# Melhore o jogo do desafio 28 onde o computador
# vai pensar num NÚMERO ENTRE ZERO E DEZ .
# Só que agroa o jogador vai tentar adivinhar até
# acertar, mostrando no final quantos palpites 
# foram necessários para vencer

from random import randint
from time import sleep
computador = randint(0, 11) #  sorteia numero
print('Pensei no número {}'.format(computador)) 
print('-=-' * 20)
print('Vou pensar em número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))  #  Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
#else:
#    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador,jogador))
count = 0
while jogador != computador:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador,jogador))
    jogador = int(input('Em que número eu pensei? '))  #  Jogador tenta adivinhar
    count += 1
    print('PROCESSANDO...')
    sleep(2)
    if jogador == computador:
        print('PARABÉNS! Você conseguiu me vencer!')
        print('foram necessários {} palpites'.format(count + 1))
