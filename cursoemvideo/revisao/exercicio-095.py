''' Aprimore o DESAFIO 093 para que ele 
    funcione com vários jogadores, 
    incluindo um sistema de visualização
    de detalhes do aproveitamento de 
    cada jogador. '''

jogador = dict()
partidas = list()
equipe = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    jogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, jogos):
        partidas.append(int(input(f'Quantos gols na partida {c}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    equipe.append(jogador.copy())
    resposta = str(input('Quer continuar? '))
    while resposta not in 'SsNn': 
        print('Responda apenas S ou N.')
        resposta = str(input('Quer continuar? '))
    if resposta in 'Nn':
        break
print('-' * 40)
print(' cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(equipe):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(equipe):
        print(f'ERRO! Não existe jogador com o código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {equipe[busca]["nome"]}')
        for i, g in enumerate(equipe[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')