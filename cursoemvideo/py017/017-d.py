#!/usr/bin/env python3


# h : hipotenusa
# co : cateto oposto
# ca : cateto adjacente
import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(h))