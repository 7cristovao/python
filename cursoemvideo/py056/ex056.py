#!/usr/bin/env python3


# Desenvolva um programa que leia o NOME, IDADE  e SEXO
# de QUATRO PESSOAS. No final do programa, mostre:

# (1) A MÉDIA DE IDADE do grupo
# (2) Qual é o nome do homem MAIS VELHO
# (3) Quantas mulheres tem MENOS DE 20 anos

s_idade = 0
c_idade = 0
menor_idade = 0
maior_idade = 0
menor_nome = 0
maior_nome = 0
c_sexo_m = 0
c_sexo_f = 0
c_mm20a = 0
plural = '-'
for p in range(1, 5):
    nome = str(input('Nome {}: '.format(p)))
    idade = int(input('Idade {}: '.format(p)))
    sexo = str(input('Sexo homem/mulher {}: '.format(p)))
    s_idade += idade
    c_idade += 1

    if sexo == 'homem':
        c_sexo_m += 1
    elif sexo == 'mulher':
        c_sexo_f += 1
        if idade < 20:
            c_mm20a += 1
    else:
        print('Digite novamente')
    if p == 1: 
        menor_idade = idade
        maior_idade = idade
    else:
        if idade > maior_idade:
            maior_idade = idade
            maior_nome = nome
        if idade < menor_idade:
            menor_idade = idade
            menor_nome = nome

media_idade = s_idade / c_idade   

if sexo == 'homem':
    artigo = 'o'
elif sexo == 'mulher':
    artigo = 'a'
else:
    artigo = ''

mulheres_menores_que_20_anos = c_mm20a

print('A média de idade do grupo é de {} anos'.format(media_idade))
print('{} {} mais velh{} tem {} anos e se chama {}'.format(artigo, sexo, artigo, maior_idade, maior_nome))
print('Ao todo são {} mulher(es) com menos de 20 anos'.format(mulheres_menores_que_20_anos))
