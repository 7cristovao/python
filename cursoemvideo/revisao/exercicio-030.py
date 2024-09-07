''' Crie um programa
    que leia um número 
    inteiro e mostre 
    na tela se ele é 
    PAR ou ÍMPAR. '''

num = int(input('Digite um número inteiro: '))
parOuImpar = num % 2

if parOuImpar == 0:
    print(f'{num} é par.')
else:
    print(f'{num} é ímpar.')