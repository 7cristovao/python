#!/usr/bin/env python3

# {1}
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)

num.remove(4)  # item q n�o existe d� erro
			 # remove �ndice espec�fico
			 # para remover segundas ou mais ocorr�ncias utilize o la�o

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
	print('N�o achei o n�mero 5')
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
	
# se quiser tamb�m o �ndice (a chave)
for c, v in enumerate(valores):
	print(f'Na posi��o {c} encontrei tamb�m o valor {v}...', end='')
print('Cheguei ao final da lista.')
