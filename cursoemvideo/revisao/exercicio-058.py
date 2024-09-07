''' Melhore o jogo do desafio 28 onde
    o computador vai "pensar" em um 
    número entre 0 e 10. Só que agora
    o jogador vai tentar adivinhar 
    até acertar, mostrando no final 
    quantos palpites foram necessários
    para vencer. '''

from random import randint

numeroJogador = -1
numeroComputador = randint(0,10)
tentativas = 0
while numeroJogador != numeroComputador:
    numeroJogador = int(input('Digite um valor: '))
    tentativas = tentativas + 1
print(f'Parabéns! Você adivinhou o valor! Foram necessárias {tentativas} tentativas')
