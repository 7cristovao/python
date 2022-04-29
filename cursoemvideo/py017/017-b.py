#!/usr/bin/env python3


# h : hipotenusa
# co : cateto oposto
# ca : cateto adjacente
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h =((co ** 2) + (ca ** 2)) ** (1/2)
print('A hipotenusa vai medir {}'.format(h))