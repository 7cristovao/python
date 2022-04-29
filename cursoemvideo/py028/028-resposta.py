#!/usr/bin/env python3


from random import randint
from time import sleep
computador = randint(0, 5)  #  sorteia numero
print('Pensei no número {}'.format(computador)) 
print('-=-' * 20)
print('Vou pensar em número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))  #  Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador,jogador))


# OBSERVAÇÃO: ESTE PROGRAMADOR IGNOROU OS ERROS