#/!usr/bin/env python3


# Aprimore o DESAFIO 86, mostrando no final:


# A) A SOMA de todos os VALORES PARES digitados

# B) A SOMA dos valores da TERCEIRA COLUNA

# C) O MAIOR valor da SEGUNDA LINHA
	
x = [[0,10,20],[0,11,21],[0,12,22]]
sa = 0
sb = 0
m = []
for l in range(0, 3):
	for c in range(0,3):
	    #print(x[l][c])
	    if x[l][c] % 2 == 0:
	        sa = x[l][c] + sa
	    if c == 2:
	    	#print(x[l][2])
	    	sb = x[l][c] + sb
	    if c == 1:
	    	#print(x[l][1])
	    	m.append(x[l][1])
print(f'soma dos pares = {sa}')
print(f'soma n da col3 = {sb} ')
print(f'maior da col2 = {max(m)}')

