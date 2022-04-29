#!/usr/bin/env python3


# Crie um programa que le varios numeros inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a CONDIÇÃO DE PARADA. No final mostre QUANTOS NÚMEROS
# foram digitados e qual foi a SOMA entre eles
# (tire o flag) #

soma = cont = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores foi {soma}!')
