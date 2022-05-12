#!usr/bin/env python3


# Digitar valores para colocar dentro de LISTA
valores = list()   # ou valores = []
for cont in range(0, 5):
	valores.append(int(input('Digite um valor: ')))
	
for c, v in enumerate(valores):
	print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')