''' Faça um programa
    que leia um número de
    0 a 9999 e mostre na
    tela cada um dos 
    dígitos separados.

    Ex:
    Digite um número: 1834

    unidade: 4
    dezena: 3
    centena: 8
    milhar: 1 '''

num = str(input('Digite um número de 0 a 9999: '))
print(f'unidade: {num[3]}')
print(f'dezena: {num[2]}')
print(f'centena: {num[1]}')
print(f'milhar: {num[0]}')