''' Faça um programa que
    leia o comprimento do
    cateto oposto e do
    cateto adjacente de 
    um triângulo retângulo,
    calcule e mostre o 
    comprimento da hipotenusa. '''

from math import sqrt

catetoOposto = float(input('Digite o comprimento do cateto oposto: '))
catetoAdjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = sqrt(catetoOposto ** 2 + catetoAdjacente ** 2)

print(f'O comprimento da hipotenusa é de {hipotenusa:.2f} cm.')
