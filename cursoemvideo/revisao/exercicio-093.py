''' Crie um programa que gerencie o aproveitamento de 
    um jogador de futebol. O programa vai ler o nome
    do jogador e quantas partidas ele jogou. Depois
    vai ler a quantidade de gols feitos em cada 
    partida. No final, tudo isso será guardado em
    um dicionário, incluindo o total de gols feitos
    durante o campeonato. '''

nome = str(input('Nome do Jogador: '))
jogos = int(input(f'Quantas partidas {nome} jogou: '))
gols = []
for c in range(0, jogos):
    gols.append(int(input(f'Quantos gols na partida {c}: ')))
total = sum(gols)
desempenho = dict()
desempenho = {'nome': nome, 'gols': gols, 'total': total}
print('-=' * 30)
print(desempenho)
print('-=' * 30)
for k, v in desempenho.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {desempenho["nome"]} jogou {jogos} partidas.')
for c in range(0, jogos):
    print(f'   => Na partida {c}, fez {gols[c]} gols')
print(f'Foi um total de {desempenho["total"]} gols.')