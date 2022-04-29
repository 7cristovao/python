#!/usr/bin/env python3

# Faça um programa que lê um valor em:
# quilômetros 
# hectômetros 
# decâmetros 
# metros 
# decímetros
# centímetros
# milímetros 

# d : distância
d = float(input('Uma distância em metros: '))
print('A medida de {:.1f}m corresponde a \n{:.3f}km \n{:.2f}hm \n{:.1f}dam \n{:.0f}m \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(d,d*10**-3,d*10**-2,d*10**-1,d*10**0,d*10**1,d*10**2,d*10**3,d*10**4))
