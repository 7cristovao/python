#!/usr/bin/env python3


# Crie um programa que simula o funcionamento
# de um CAIXA ELETRONICO. No inicio, pergunte
# ao usuário qual será o VALOR A SER SACADO
# (número inteiro) e o programa vai indormar
# quantos CÉDULAS de cada valor serão entregues.

# OBSERVAÇÃO: considere que o caixa possui cédulas
# de R$ 50, R$ 20, R$ 10 e R$ 1.

# OBSERVAÇÃO: exercício já resolvido na linguagem C++

x = 0
c_01 = 0
c_10 = 0
c_20 = 0
c_50 = 0
while True:
    x = int(input('V saque? '))
    c_50 = int(x / 50)
    c_20 = int((x - (c_50 * 50)) / 20)
    c_10 = int((x - (c_50 * 50) - (c_20 * 20)) / 10)
    c_01 = int(x - (c_50 * 50) - (c_20 * 20) - (c_10 * 10))
    break
print('c_50 = {}'.format(c_50))
print('c_20 = {}'.format(c_20))
print('c_10 = {}'.format(c_10))
print('c_01 = {}'.format(c_01))
    
