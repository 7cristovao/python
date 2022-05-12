#!usr/bin/env python3


# LISTAS, PECULIARIDADE DO PYTHON
a = [2, 3, 4, 7]
b = a
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')

# NÃO SE TRATA DE UMA CÓPIA DE LISTA, MAS SIM
# DE UMA LIGAÇÃO ENTRE LISTAS, 
# (quase que um relacionamento de BD)


# {1}
# PARA CRIAR UMA CÓPIA
a = [2, 3, 4, 7] 
b = a[:]   # <<<<<<<<<<<<<<< essa linha fica assim
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')