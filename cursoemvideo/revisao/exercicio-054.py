''' Crie um programa que leia 
    o ano de nascimento de sete
    pessoas. No final, mostre quantas 
    pessoas ainda não atingiram a
    maioridade e quantas já são 
    maiores. '''

from datetime import datetime

# armazena em uma variável o ano atual
anoAtual = datetime.now().year

# lê o ano de nascimento de 7 pessoas
#
qtePessoasQueNaoAtingiramAMaioridade = 0
qtePessoasQueAtingiramAMaioridade = 0
for c in range(1, 8):
    anoDeNascimento = int(input('Digite o ano de nascimento: '))
    if anoAtual - anoDeNascimento >= 18:
        qtePessoasQueAtingiramAMaioridade = qtePessoasQueAtingiramAMaioridade + 1
    else:
        qtePessoasQueNaoAtingiramAMaioridade = qtePessoasQueNaoAtingiramAMaioridade + 1
print(f'A quantidade de pessoas que atingiram a maioridade é de {qtePessoasQueAtingiramAMaioridade}')
print(f'A quantidade que não atingiram a maioridade é de {qtePessoasQueNaoAtingiramAMaioridade} pessoa')
print('FIM')