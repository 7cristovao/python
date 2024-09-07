''' Desenvolva um programa que leia
    o primeiro termo e a razão de uma 
    PA. No final, mostre os 10 primeiros
    termos dessa progressão. '''

# lê a informação do primeiro termo
a1 = int(input('Digite o PRIMEIRO TERMO de uma progressão aritmética: '))

# lê a informação da razão
r = int(input('Digite a RAZÃO de uma progressão aritimética: '))

# exibe os 10 primeiros termos desta progressão
for c in range(1, 11):
    print(f'a_{c} = {a1 + (c - 1) * r}')
print('Fim!')