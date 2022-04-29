#!/usr/bin/env python3


# Crie um programa que leia DOIS VALORES e mostre um MENU na tela 
# [1] somar 
# [2] multiplicar 
# [3] maior
# [4] novos números
# [5] sair do programa
#
# Seu programa deverá realizar a aparição solicitada
# em cada caso.

# -----------------
# v1 : valor1
# v2 : valor2
# ó : opção

x1 = 0
x2 = 0
ó = 0
while ó != 5:
    x1 = int(input('Digite um valor: '))
    x2 = int(input('Digite outro valor: '))
    ó = int(input('''

    Escolha uma opção para:

    [1] somar 
    [2] multiplicar 
    [3] maior
    [4] novos números
    [5] sair do programa
    
    '''))
    
    if ó == 1:
        print('A soma é {}'.format(x1 + x2))
    elif ó == 2:
        print('A multiplicação é {}'.format(x1 * x2))
    elif ó == 3:
        if x1 == x2:
            print(x1 == x2)
            print('A 1ª variável é igual a 2ª incógnita')
        else:
            if x1 > x2:
                print(x1 > x2)
                print('A 1ª variável {} é maior que a 2ª incógnita '.format(x1))
            elif x2 > x1:
                print(x2 > x1)
                print('A 2ª variável {} é maior que a 1ª incógnita '.format(x2))
            else:
                print('O progr/algorit ignorante sequer chega neste processo')
    elif ó == 5:
        print('Você saiu do programa.')
    elif ó == 4:
        print('Digite novos números')
    else:
        print('Digite novamente')
