#!/usr/bin/env python3
# coding=utf-8

# Crie uma TUPLA preenchida com os 20(21) PRIMEIROS
# colocados da Tabela do CAMPEONATO BRAS DE FUT
# na ordem de colocaçao. Depois mostre:
# A) Apenas os 5 PRIMEIROS colocados
# B) Os ÚLTIMOS 4 colocados da tabela
# C) Uma lista com os times em ORDEM ALFABÉTICA
# D) Em que POSIÇÃO na tabela esta o time da CHAPECOENSE

# bras : lista com os 21 primeiros
# braz : transforma a lista 'bras' em string
# pos  : posicao na tabela

times = ('America Mineiro', 'Athletico Paranaense', 'Sport', 'Atletico Goianiense',
'Atletico Mineiro', 'Bahia', 'Red Bull Bragantino', 'Chapecoense', 'Ceara',
'Cuiaba', 'Fortaleza', 'Gremio', 'Internacional', 'Juventude', 'Santos', 'SaoPaulo', 'Flamengo', 'Fluminense', 'Corinthians', 'Palmeiras')
print('\n\nOs cinco primeiros colocados: {}'.format(times[0:5]))
print('\n\nOs ULTIMOS 4 colocados da tabela: {}\n\n'.format(times[-1:-5:-1]))
print('\n\nTimes em ordem alfabetica: {}'.format(sorted(times)))
#  o metodo sorted nao altera a ordem da tupla
print('\n\n')
print("O Chapecoense esta na posicao {}. ".format(times.index('Chapecoense')+1))
print('\n\n')
