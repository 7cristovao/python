#!/usr/bin/env python3

# {1}
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)

num.remove(4)  # item q não existe dá erro
			 # remove índice específico
			 # para remover segundas ou mais ocorrências utilize o laço

print(num)
print(f'Essa lista tem {len(num)} elementos.')

# {2}
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 5 in num:
	num.remove(5)
else:
	print('Não achei o número 5')
print(num)
print(f'Essa lista tem {len(num)} elementos.')

# {3}
# Pode-se criar uma lista vazia assim: 
# valores = list ()
# ou assim
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
	print(f'{v}...', end='')
	
# se quiser também o índice (a chave)
for c, v in enumerate(valores):
	print(f'Na posição {c} encontrei também o valor {v}...', end='')
print('Cheguei ao final da lista.')
