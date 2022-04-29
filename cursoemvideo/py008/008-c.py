#!/usr/bin/env python3

# d : distância
d = float(input('Uma distância em metros: '))
print('A medida de {:.1f}m corresponde a \n{:.4f}km \n{:.3f}hm \n{:.2f}dam \n{:.1f}m \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(d,d*1e-3,d*1e-2,d*1e-1,d*1e0,d*1e1,d*1e2,d*1e3))
