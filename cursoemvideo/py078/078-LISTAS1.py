#!usr/bin/env python3


# LISTAS
# lanche = ['h', 's', 'p', 'b']
# lanche[3] = 'g'
# FICA ASSIM
# lanche = ['h', 's', 'p', 'g']

## h : hamburguer #
## s : suco  
## p : pizza
## b : bolo(pudim)
## g ; gelado(picol�)
## k : cookie
## d : cachorro-quente(dog)

# m�todos
# lanche.list
# lanche.append('k')  ## adiciona item k no final da lista
## M�todo PUSH?
# lanche.insert(0,'d')  ## adiciona item d na lista na posi��o ZERO antes de 'h' 
#                                ## e empurra 'h' pra frente e os outros tambem
##APAGAR ELEMENTOS
# del lanche[3]    ## eliminar o lanche 3
# lanche.pop(3)   ## normalmente para eliminar o �ltimo elemento, mas aki tem 3
# lanche.remove('p')  ## elimina pelo nome do elemento (conte�do)
## ELIMINA o CONTE�DO, ELIMINA O VALOR do �NDICE e REFAZ o �NDICE

# lanche.pop()   ## eliminar o �ltimo elemento

## no caso de tentar remover um indice que n�o existe retorna erro use
# if 'p' in lanche:
#      lanche.remove('p')

# valores = list(range(4, 11))
#
# cria lista [4, 5, 6, 7, 8, 9, 10]
#                 0  1  2  3  4  5    6      s�o os �ndices da vari�vel valor
#

# valores = list(range(4, 11, 2)  # pula de dois em dois

# valores = [8, 7, 3, 6, 5, 2, 1]   # cria lista
# valores.sort()  # ordena todos os valores
# valores.sort(reverse=True)  #  valores ficam ordenados na ordem reversa
# len(valores) # igual a 7, quanta a qte de elementos da lista
