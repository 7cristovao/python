#!/usr/bin/env python3


# Crie um programa onde o usuario possa digitar varios 
# VALORES NUMERICOS e cadastre-os um uma LISTA.
# Caso o numero ja exista la dentro ela 
# NAO SERA ADICIONADA. 
# No final serao exibidos todos os VALORES UNICOS digitados, em 
# ORDEM CRESCENTE.
# p : posicao

numeros = []
p = 0
while p != 999:
    numeros.append(int(input('Dig. o valor: '.format(p))))
    print(numeros)
    print(numeros[-1::1])
    n = numeros[-1::1]
    if 1 in numeros:
        numeros.remove(n)
    else:
        print('Nao achei o numero {}'.format(n))
print(num)
