#!/usr/bin/env python3
# coding = utf-8

# Faca um programa que le um NUMERO INTEIRO e diga se ele 
# eh ou nao um NUMERO PRIMO

# 2/1 = 2
# 2/2 = 1   
# 3/3 = 1
# 3/1 = 3
# 5/1 = 5
# 5/5 = 1

# 4/1 = 4  ... n / 1 = n
# 4/2 = 2  ... n / 2 = 2 
# 4/4 = 1  ... n / 4 = 1

n = int(input('Digite um no. inteiro: '))
c = n
cont = 0
for n in range(1, n + 1):
    if c % n == 0:
        cont += 1
        print('{} / {} = {:.0f}     linha no. {}'.format(c, n, c / n, cont))
if cont == 2:
    print('Eh um numero primo')
else:
    print('Nao eh um numero primo')
print('fim')
