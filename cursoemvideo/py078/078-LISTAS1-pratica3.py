#!usr/bin/env python3


# LISTAS, PECULIARIDADE DO PYTHON
a = [2, 3, 4, 7]
b = a
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')

# N�O SE TRATA DE UMA C�PIA DE LISTA, MAS SIM
# DE UMA LIGA��O ENTRE LISTAS, 
# (quase que um relacionamento de BD)


# {1}
# PARA CRIAR UMA C�PIA
a = [2, 3, 4, 7] 
b = a[:]   # <<<<<<<<<<<<<<< essa linha fica assim
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')