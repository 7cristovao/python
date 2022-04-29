#!/usr/bin/env python3


# 58

# Melhore o jogo do desafio 28 onde o computador
# vai pensar num NÚMERO ENTRE ZERO E DEZ .
# Só que agroa o jogador vai tentar adivinhar até
# acertar, mostrando no final quantos palpites 
# foram necessários para vencer

from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
print('Acertou com {} tentativas. Parabéns!'.format(palpites))

