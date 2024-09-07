''' Faça um programa que leia 
    um número qualquer e mostre
    o seu fatorial. 
    
    Ex:
    5! = 5x4x3x2x1 = 120 '''

fatorial = 1
num = int(input('Digite um número para calcular seu fatorial: '))
cont = num
while cont > 0:
    fatorial = fatorial * cont
    cont = cont - 1
print(f'{num}! = {fatorial}')
print(f'Fim do programa')