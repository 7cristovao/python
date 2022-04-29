#!/usr/bin/env python3

'''
x    : frase
m    : ponto medio
mm   : ponto medio menos um
mmm  : ponto medio mais um
c    : conta quantidade de caracteres da frase sem os espacos

cont : contador do loop

'''
x = input('Digite uma frase: ')
print(type(x))
print(x)
x = x.upper()
print(x)
x = x.replace(' ', '')
print(x)
c = len(x)
print(c)
if c % 2 == 1:
    if c > 2:
        # mont = 0
        cont = 0
        for cont in range(0, c):
            #print(x[cont])
            #print(x[cont-1])
            if x[cont] == x[cont-1]:
                #print(f'ind {cont} valor {x[cont]} == {x[cont-1]} ind {cont-1}')
                print('É um palindromo')
                break
            else:
                print('Não é um palindromo')
                break
