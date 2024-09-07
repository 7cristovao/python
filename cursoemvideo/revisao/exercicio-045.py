''' Crie um programa que faça o 
    computador jogar Jokenpô
    com você. '''

from random import randint # importa a função 'randint' da biblioteca 'random'

# imprime as opções
print('''\n
JOKENPÔ\n 
[1] para PEDRA 
[2] para PAPEL
[3] para TESOURA \n''')

# solicita ao usuário para dar entrada em uma das opções
escolhaDoJogador = int(input('Escolha uma opção: '))

# computador sorteia aleatoriamente uma opção
escolhaDoComputador = randint(1,3)

# exibe as opções escolhidas pelo usuário e pelo computador
if escolhaDoJogador == 1:
    print('\nVocê escolheu PEDRA')
elif escolhaDoJogador == 2:
    print('\nVocê escolheu PAPEL')
elif escolhaDoJogador == 3:
    print('\nVocê escolheu TESOURA')
else:
    print('\nOpção inválida')
if escolhaDoComputador == 1:
    print('O computador escolheu PEDRA')
elif escolhaDoComputador == 2:
    print('O computador escolheu PAPEL')
elif escolhaDoComputador == 3:
    print('O computador escolheu TESOURA')

# exibe quem venceu
if escolhaDoJogador == escolhaDoComputador:
    print('\nEmpatou! Jogue novamente!')
elif (escolhaDoJogador == 1 and escolhaDoComputador == 2) or (escolhaDoJogador == 2 and escolhaDoComputador == 3) or (escolhaDoJogador == 3 and escolhaDoComputador == 1):
    print('\nComputador venceu!')
elif (escolhaDoJogador == 1 and escolhaDoComputador == 3) or (escolhaDoJogador == 2 and escolhaDoComputador == 1) or (escolhaDoJogador == 3 and escolhaDoComputador == 2):
    print('\nVocê venceu!')
else:
    print('\nFim de jogo!')