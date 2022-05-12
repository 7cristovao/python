#!/usr/bin/env python3


# Crie um programa que tenha uma TUPLA unica com
# NOMES DE PRODUTOS e seus respectivos PRECOS
# na sequencia.

# No final, mostre uma listagem de precos, organizando
# os dados em forma TABULAR.


listagem = (
'Lapis', 1.75,
'Borracha', 2,
'Caderno', 15.90,
'Estojo', 25,
'Transferidor', 4.20,
'Compasso', 9.99,
'Mochila', 120.32,
'Canetas', 22.30,
'Livro', 34.90)
print(f'{"LISTAGEM DE PRECOS":^40}') #  centralizado
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print('{:.<30}'.format(listagem[pos]), end=' ')  # alinhado a esq
    else:
        print('R$ {:>7.2f} '.format(listagem[pos]))  # alinhado a dir
       # print('R$ {:>7.2f} '.format(listagem[pos]))  # ele poe os pts no preco 
