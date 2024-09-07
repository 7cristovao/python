''' Faça um programa que 
    leia um ângulo qualquer 
    mostre na tela o valor
    do seno, cosseno e
    tangente desse ângulo. '''

from math import sin, cos, tan, radians

valorDoAngulo = float(input('Digite o valor do ângulo: '))
print(f'O valor do seno de {valorDoAngulo} é de {sin(radians(valorDoAngulo)):.2f}.')
print(f'O valor do cosseno de {valorDoAngulo} é de {cos(radians(valorDoAngulo)):.2f}.')
print(f'O valor da tangente de {valorDoAngulo} é de {tan(radians(valorDoAngulo)):.2f}.')
