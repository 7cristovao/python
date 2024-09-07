''' Escreva um programa que leia um numero n 
    inteiro qualquer e mostre na tela os n 
    primeiros elementos de uma Sequencia
    de Fibonacci. 
    
    Ex:
    0 → 1 → 1 → 2 → 3 → 5 → 8 '''

print('Sequência de Fibonacci')
n = int(input('Quantos termos você quer mostrar? '))
termo1 = 0
termo2 = 1
print(f'{termo1} → {termo2}', end='')
cont = 3
while cont <= n:
    termo3 = termo1 + termo2
    print(f' → {termo3}', end='')
    termo1 = termo2
    termo2 = termo3
    cont += 1
print('\nfim')
