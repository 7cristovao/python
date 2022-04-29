#!/usr/bin/env python3

distancia = float(input('Uma distância em metros: '))
km = distancia * 0.001      #   km = distancia * 10 ** -3
hm = distancia * 0.01       #   hm = distancia * 10 ** -2
dam = distancia * 0.1       #  dam = distancia * 10 ** -1
m = distancia               #    m = distancia * 10 ** 0
dm = distancia * 10         #   dm = distancia * 10 ** 1
cm = distancia * 100        #   cm = distancia * 10 ** 2
mm = distancia * 1000       #   mm = distancia * 10 ** 3

print('A medida de {:.1f}m corresponde a \n{:.3f}km \n{:.2f}hm \n{:.1f}dam \n{:.0f}m \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(distancia,km,hm,dam,m,dm,cm,mm))
