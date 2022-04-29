#!/usr/bin/env python3



# SOMATÓRIO
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
#   s += 1     #  VAI CONTAR CADA INPUT
    s += n     #  VAI SOMAR OS VALORES INSERIDOS (INCLUINDO A FLAG)
print('A soma vale {}'.format(s))

# o if, break resolve o problema da gambiarra
# ele soma sem somar
# break sai de um ENQUANTO