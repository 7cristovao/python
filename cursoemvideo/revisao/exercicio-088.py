''' Faça um programa que ajude um jogador da
    MEGA SENA a criar palpites. O programa vai
    perguntar quantos jogos serão gerados e 
    vai sortear 6 números entre 1 e 60 para 
    cada jogo, cadastrando tudo em uma lista
    composta. '''

from random import randint

print('PALPITES PARA MEGA SENA')
qteJogos = 0
qteJogos = int(input('Quantos jogos você quer? '))
numerosSorteados = []
jogosSorteados = []
for c in range(0, qteJogos):
    for d in range(0, 6):
        numerosSorteados.append(randint(1, 60))
    jogosSorteados.append(numerosSorteados[:])
    numerosSorteados.clear()
print(f'Os jogos foram {jogosSorteados}')
print('FIM')        
    
