#!/usr/bin/env python3


# Faca um programa que ajude um jogador da MEGA SENA a 
# criar palpites. O programa vai perguntar 
# QUANTOS JOGOS serao gerados e vai sortear
# SEIS NUMEROS ENTRE 1 e 60
# para cada jogo, cadastrando tudo em uma LISTA COMPOSTA
# determine N jogos

from random import randint

lista = list() #(5)
#(11)
quant = int(input('Quantos jogos você quer que eu sorteie?: '))
tot = 1 #(12)
jogos = list() #(14)
while tot <= quant: #(13) identa o restante
	cont = 0 #(2)
	while True: #(3)
		num = randint(1, 60) #(1)
		if num not in lista: #(4)
			lista.append(num) #(6...)
			cont = cont + 1
		if cont >= 6:
			break #(9) roda
	lista.sort() #(10) roda
	jogos.append(lista[:]) #(15) faz copia da lista
	lista.clear() #(16) limpa a lista dados tao em jogos
	tot = tot + 1 #(17)
	#mudar placeholder lista para jogos
	print(f'Os numeros sorteados foram {jogos}')

# fazer varias vezes

