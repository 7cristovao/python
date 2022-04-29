#!/usr/bin/env python3
# encoding: utf-8


# lê TRES número e mostra o maior e o menor

x1 = int(input('Primeiro valor: '))
x2 = int(input('Segundo valor: '))
x3 = int(input('Terceiro valor: '))

if x1 < x2 < x3:
    print('O menor valor digitado foi {}'.format(x1))
    print('O maior valor digitado foi {}'.format(x3))
elif x1 < x3 < x2:
    print('O menor valor digitado foi {}'.format(x1))
    print('O maior valor digitado foi {}'.format(x2))
elif x2 < x1 < x3:
    print('O menor valor digitado foi {}'.format(x2))
    print('O maior valor digitado foi {}'.format(x3))
elif x2 < x3 < x1:
    print('O menor valor digitado foi {}'.format(x2))
    print('O maior valor digitado foi {}'.format(x1))
elif x3 < x2 < x1:
    print('O menor valor digitado foi {}'.format(x3))
    print('O maior valor digitado foi {}'.format(x1))
elif x3 < x1 < x2:
    print('O menor valor digitado foi {}'.format(x3))
    print('O maior valor digitado foi {}'.format(x2))
else:
    print('Insira valores inteiros')