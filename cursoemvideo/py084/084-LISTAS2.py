#!/usr/bin/env python3


# LISTAS PARTE DOIS:  LISTAS DENTRO DE LISTAS
#  
#
#
#
#
#         pessoas
#          .-----------------------------.
#          | .-----------.   .--------.  |
#          | | 'Pedro' |  |  25  |  | 
#          | '-----------'    '--------'  |
#          |      0             1      |
#          '------------------------------'
#                        0
#  
#  {1} CÓPIA DA VARIÁVEL COMPOSTA DADOS
pessoas = list()
pessoas.append(dados[:])

#
#  vai ter
#  
#     'Pedro', 25 |  'Maria, 19   |   'João', 32  
#          0       1          0      1         0       1
#           ZERO         HUM              DOIS
#               0                1                     2
#
#
# {2} ABRE UM COLCHETÃO
#

pessoas=[['Pedro',25],['Maria',19],['João',32]]

print(pessoas[0][0])  # exibe Pedro
print(pessoas[1][1])  # exibe 19
print(pessoas[2][0])  # exibe João
print(pessoas[1])       # exibe ['Maria',19]







