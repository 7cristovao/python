#!/usr/bin/env python3


#  Faça um programa que leia o PESO de CINCO PESSOAS.
# No final, mostre qual foi o MAIOR e o MENOR peso.

# maior : maior_peso
# menor : menor_peso

# p : pessoa

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {} pessoa: '.format(p)))
    if p == 1:  # (1) (1.1) (2)
        maior = peso  # (3)
        menor = peso  # (4)
    else:  # (5)
        if peso > maior:  # (6)
            maior = peso  # (7)
        if peso < menor:  # (8)
            menor = peso  # (9)
print('O maior peso lido foi de {}kg'.format(maior))
print('O menor peso lido foi de {}kg'.format(menor))

# (1) Quando eu quero maior e menor eu vou verificar se é a primeira ocorrência
# (1.1) Porque eu não li mais nada diferente disso

# (2) É o peso da primeira pessoa, acabei de ler o peso da primeira pessoa

# (3) O maior peso vai passar a ser o peso

# (4) O menor peso também vai passar a ser o peso

# (5) SENÃO

# (6) SE o peso que eu acabei de ler for maior do que meu maior peso

# (7) O maior peso passa a ser o peso que eu acabei de ler

# (8) SE o peso que eu acabei de ler for menor do que meu menor peso

# (9) O menor peso passa a ser o peso que eu acabei de ler
