#!/usr/bin/env python3


# Faça um programa sobre uma locadora de carros que lê:
# (1) Quantos dias o carro ficou ou vai ser alugado? 
# (2) Qual a distância percorrida? 
# Que também calcule e apresente o total a pagar: 
# (3) Com a diária no valor de R$ 60,00 + km rodado no valor de 0.15
diarias = int(input('Quantos dias alugados? '))
distanciaPercorrida = float(input('Quantos quilometros rodados? '))
total = diarias * 60 + distanciaPercorrida * 0.15
print('O total a pagar eh de R${:.2f}'.format(total))