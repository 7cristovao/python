''' Faça um programa que jogue par ou ímpar com o 
    computador. O jogo só será interrompido quando
    o jogador PERDER, mostrando o total de vitórias
    consecutivas que ele conquistou no final do jogo. '''

from random import randint

cont = 0
while True:
    escolhaDoJogador = str(input('''
                                Escolha:
                                P para par ou
                                I para ímpar: ''')).upper().strip()
    if escolhaDoJogador not in 'PI':
        print('Opção errada!')
        break
    elif escolhaDoJogador == 'P':
        escolhaDoJogador = 'PAR'
        escolhaDoComputador = 'ÍMPAR'
    else:
        escolhaDoJogador = 'ÍMPAR'
    print(f'Você escolheu {escolhaDoJogador}')
    numeroDoJogador = int(input('Escolha um número de 0 até 5: '))
    numeroDoComputador = randint(0,5)
    print(f'O computador escolheu {numeroDoComputador}')
    soma = numeroDoJogador + numeroDoComputador
    if soma % 2 == 0:
        soma = 'PAR'
    else:
        soma = 'ÍMPAR'
    if escolhaDoJogador == soma:
        print(f'Você venceu!')
        cont = cont + 1
    else:
        print(f'O computador venceu!')
        print(f'Parabéns, você ganhou {cont} vez(es)!')
        break

