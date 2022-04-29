#!/usr/bin/env python3


# Escreva um algoritmo que  converte a temperatura de Celsius para Farenheit

# c : celsius
# f : farenheit
c = float(input('Informe a temperatura em °C: '))
f = (9/5)*c + 32

print('A temperatura de {}°C corresponde a {}°F'.format(c,f))
