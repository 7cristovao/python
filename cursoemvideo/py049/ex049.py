#!/usr/bin/env python3


# Refaça o exercício 9, mostrando a TABUADA de um número
# que o usuário escolher, só que agora utilizando
# um LAÇO FOR.

n = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    # print(n)
    print('{} x  {:2} = {}'.format(n, c, n*c))

