# 0-1-1-2-3-5-8

# Crie um programa que leia VÁRIOS NÚMEROS
# inteiros pelo teclado. O programa só vai parar quando o 
# usuário digitar o valor 999,  que é a CONDIÇÃO DA PARADA
# No final mostre QUANTOS NÚMEROS foram digitados e qual foi
# a soma entre eles (DESCONSIDERANDO O FLAG [esse 999])

i = 0
n = 0
while n != 999:
    n = int(input('Digite 999 para parar: '))
    i = i + 1
print('Foram digitados {} nº'.format(i-1))
print('fim')

