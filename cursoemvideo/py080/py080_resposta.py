#!/usr/bin/env python3


# Crie um prg onde o usuario possa digitar cinco VALORES
# NUMERICOS  e cadastre-os em uma LISTA, JA NA 
# POSICAO CORRETA  de insercao (sem usar o SORT).

# No final mostre a LISTA ORDENADA na tela

lista = []
for c in range(0, 5):
     n = int(input('Dig. o valor: '))
     if c == 0: #  or n > lista[-1]: # se for o primeiro valor, pode dar o append
         lista.append(n)
     elif n > lista[-1]:  # se usar o or na linha 13 apaga aqui
         lista.append(n)  # se usar o or na linha 13 apaga aqui
         print('Adicionado ao final da lista')
     else:
         posicao = 0
         while posicao < len(lista):
             if n <= lista[posicao]:
                 lista.insert(posicao, n)
                 print('Adicionado na posicao {} da lista...'.format(posicao))
                 break
             posicao += 1
print('Os valores digitados em ordem foram {}'.format(lista))
 

 
