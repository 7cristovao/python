#!/usr/bin/env python3
# coding = utf-8

# Faca um programa que le um NUMERO INTEIRO e diga se ele 
# eh ou nao um NUMERO PRIMO

num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('Eh um numero primo')
else:
    print('Nao eh um numero primo')
print('fim')
