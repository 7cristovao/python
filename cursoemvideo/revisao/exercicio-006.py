''' Crie um algoritmo que leia
    um número e mostre o seu dobro,
    triplo e raiz quadrada. '''
from math import sqrt

num = int(input('Digite um número: '))
print(f'O dobro deste número é igual a {num * 2}')
print(f'O triplo destre número é igual a {num * 3}')
print(f'A raiz quadrada deste número é igual a {sqrt(num):.2f}')
