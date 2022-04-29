#!/usr/bin/env python3


# Faça um programa que lê a altura e a largura de uma parede 
# e calcula a quantidade de tinta necessária para ela#

#  l : largura
#  h : altura
#  A : área
l = float(input('Largura da parede: '))
h = float(input('Altura da parede: '))
A = l * h
quantidade = 0.5 * A  #  Sabendo que um litro de tinta pinta dois metros quadrados
print('Sua parede tem o tamanho de {}x{} e sua área é de {}m²'.format(l, h, A))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(quantidade))

""" 2.5 * 1.75 = 4.375 m²

             4.375 m² = 2.1875
             1.000 m² = x

             4.375 m² x = 2.1875 l
                  x = 2.1875 / 4.375
                  x = 0.5  l/m² """
