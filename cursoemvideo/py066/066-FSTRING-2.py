#!/usr/bin/env python3


nome = 'José'
idade = '33'
salário = 987.3
print(f'O {nome:--^20} tem {idade} anos e ganha R${salário:.2f}')
#     ↆ
#     fstring para python3.6+ 



# 20       quantidade de espaços
# ^ centralizado
# -- complementado
# -> alinhado a direita
# <- alinhado a esquerda
# :.2f    duas casas decimais FLOAT

# FSTRING utilizando método de interpolação