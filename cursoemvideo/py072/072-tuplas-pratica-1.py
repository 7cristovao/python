#!/usr/bin/env python3


# () tupla  [] lista  {} dicionário

# {1}
# lanche = Hamburger
# lanche = Suco
# print(lanche)   # ele apaga o Hamburger e recebe Suco

# {2}
# lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim'  # P3.6+ aceita tupla sem ()
# print(lanche)

# {3}
# lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim') # P3.6 aceita tupla sem ()
# print(lanche[1])

# {4}
# lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')  #P3.6 aceita tupla sem ()
# print(lanche[3])

# {4}
# lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')  #P3.6 aceita tupla sem ()
# print(lanche[-2])

# {5}
# lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')  #  aceita tupla sem ()
# print(lanche[1:3])

# {6}
# lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
# print(lanche[2:])

# {7}
# lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
# print(lanche[:2])

# {8}
# lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
# print(lanche[-2:])  # começa do -2 e vai até o final

# {9}
# lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
# print(lanche)

# {10}  # comando está errado não pode ser executado
# lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
# ## Tuplas são imutáveis###
# lanche[1] = 'Refrigerante'
# print(lanche[1])

# '''Traceback (most recent call last):
#  File "072-tuplas-pratica-1.py", line 50, in <module>
#    lanche[1] = 'Refrigerante'
# TypeError: 'tuple' object does not support item assignment'''

# {11}
# lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
# for comida in lanche:
#    print(f'Ele vai comer {comida}')
# print('Ele comeu muito!')

# {12}
# PARADO O PROGRAMA AGORA SE PODE INCLUIR ELEMENTO NA TUPLA
# lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# for comida in lanche:
#    print(f'Ele vai comer {comida}')
# print('Ele comeu muito!')

# {13}
# lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# for cont in range(0, len(lanche)):
#    print(lanche[cont])
# print('Comeu pra caramba!')

# {13b}
# for comida in lanche:
#    print('Ele foi comer {}'.format(comida))
# print('Comeu pra caramba!')

# {13c}
# lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
#
# for cont in range(0, len(lanche)):
#    print(lanche[cont])
# print(f'Comeu pra caramba!')


