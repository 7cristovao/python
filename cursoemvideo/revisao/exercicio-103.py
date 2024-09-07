''' Faça um programa que tenha uma função 
    chamada ficha(), que receba dois 
    parâmetros opcionais: o nome de um
    jogador e quantos gols ele marcou.
    
    O programa deverá ser capaz de mostrar
    a ficha do jogador, mesmo que algum dado
    não tenha sido informado corretamente. '''

def ficha(nome, gols):
    if nome == '':
        return f'O jogador <desconhecido> fez {gols} gol(s) no campeonato.'
    else:
        return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


nome = str(input('Nome do Jogador: '))
gols = int(input('Número de Gols: '))
print(ficha(nome, gols))