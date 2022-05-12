#!usr/bin/env python3
#encoding: utf-8


# Crie um prog onde o usuario possa digitar SETE VALORES NUMERICOS
# e cadastre-os em uma LISTA UNICA que mantenha separados os valores PARES 
# e IMPARES. No final mostre os valores pares e impares em ordem crescente

#9876543

num = [[],[]]
x = [9,8,7,6,5,4,3]
for i in x:
	if i % 2 == 0:
		print(f'{i} eh par')
		num[0].append(i)
	elif i % 2 == 1:
		print(f'{i} eh impar')
		num[1].append(i)
	else:
		print(f'{i} eh erro')
print(num)