''' Escreva um programa que 
    faça o computador "pensar"
    em um número inteiro entre 
    0 e 5 e peça para o usuário
    tentar descobrir qual foi
    o número escolhido pelo
    computador. O programa deverá
    escrever na tela se o usuário
    venceu ou perdeu. '''

from random import randint

numeroUsuario = int(input('Escolha um número entre 0 e 5: '))
numeroComputador = randint(0,5)
print(f'Você escolheu {numeroUsuario}.')
print(f'O computador escolheu {numeroComputador}.')
if numeroUsuario == numeroComputador:    
    print(f'Você venceu!')
else:
    print(f'Você perdeu!')