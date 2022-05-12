#!usr/bin/env python3
#encoding: utf-8

# Faca um programa que le NOME E PESO de VARIAS PESSOAS
# guardando tudo em uma LISTA. No final mostre:

# A) QUANTAS pessoas foram cadastradas
# B) Uma listagem com as pessoas mais PESADAS
# C) Uma listagem com as pessoas mais LEVES

temp = list()
princ = list()

while True:
	temp.append(str(input('Digite seu nome: ')))
	temp.append(float(input('Digite seu peso: ')))
	if len(princ) == 0:
		mai = men = temp[1]
	else:
		if temp[1] > mai:
			mai = temp[1]
		if temp[1] < men:
			men = temp[1]
			
	princ.append(temp[:])
	temp.clear()
	resp = str(input('Quer continuar? (S/N) '))
	if resp in 'Nn':
		break
print(f'Os dados foram {princ}')

for p in princ:
	print(p[1])

print(f'cadastradas = {len(p)}')
print(f'\nmaior peso = {mai}. Peso de ', end = '')
for p in princ:
	if p[1] == mai:
	    print(f'[{p[0]}]', end='')
print(f'\nmenor peso = {men}. Peso de ', end = '')
for p in princ:
	if p[1] == men:
		print(f'[{p[0]}]', end='')