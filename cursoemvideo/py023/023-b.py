#!/usr/bin/env python3


n = str(input('Informe um número: '))
print('Analisando o número {}'.format(n))
#print('algarismos = ', len(n))
algarismos = len(n)
if (algarismos == 1):
    print('unidade =', n)
    print('dezena =', 0)
    print('centena =', 0)
    print('milhar =', 0)
elif (algarismos == 2):
    print('unidade =', n[1])    
    print('dezena =', n[0])
    print('centena =', 0)
    print('milhar =', 0)
elif (algarismos == 3):
    print('unidade =', n[2])    
    print('dezena =', n[1])
    print('centena =', n[0])
    print('milhar =', 0)
else:
    print('unidade =', n[(algarismos-1):algarismos])    
    print('dezena =', n[(algarismos-2)])
    print('centena =', n[(algarismos-3)])
    print('milhar = ', n[(algarismos-algarismos):(algarismos-3)])