#!/usr/bin/env python3


n = int(input('Informe um número: '))
print('Analisando o número {}'.format(n))
unidade  = n % 10
dezena   = n % 100 // 10
centena  = n % 1000 // 100
milhar   = n % 10000 // 1000
#dmilhar = n % (1 * 10 ** 5) // (1 * 10 ** 4)
#cmilhar = n % 1000000 // 100000
print('unidade = {}'.format(unidade))
print('dezena = {}'.format(dezena))
print('centena = {}'.format(centena))
print('milhar = {}'.format(milhar))
#print('dmilhar = {}'.format(dmilhar))

