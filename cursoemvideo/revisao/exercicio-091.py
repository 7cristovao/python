''' Crie um programa onde 4 jogadores 
    joguem um dado e tenham resultados 
    aleatórios. Guarde esses resultados
    em um dicionário. No final, coloque
    esse dicionário em ordem, sabendo
    que o vencedor tirou o maior número
    no dado. '''

from random import randint
from time import sleep
from operator import itemgetter

resultados = dict()
resultados = {'jogador1': 0, 'jogador2': 0, 'jogador3': 0, 'jogador4': 0}
resultados['jogador1'] = randint(1, 6)
resultados['jogador2'] = randint(1, 6)
resultados['jogador3'] = randint(1, 6)
resultados['jogador4'] = randint(1, 6)
print('Valores sorteados: ')
for k, v in resultados.items():
    print(f' {k} tirou {v} no dado.')
    sleep(1)
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
classificacao = sorted(resultados.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(classificacao):
    print(f'     {i + 1}º lugar {v[0]} tirou {v[1]} no dado.')
    sleep(1)