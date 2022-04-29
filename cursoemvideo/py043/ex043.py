#!/usr/bin/env python3


# Desenvolva um código que lê a massa e a altura de
# uma pessoa, calcula seu IMC e mostra seu status, conforme a tabela abaixo:
#
# (1) Abaixo de 18.5: abaixo do peso
# (2) Entre 18.5 e 25: peso ideal
# (3) 25 até 30: sobrepeso
# (4) 30 até 40: obesidade
# (5) Acima de 40: Obesidade mórbida #

# imc = massa do indivíduo / quadrado de sua altura

h = float(input('Qual a altura do indivíduo (em metros)? '))
m = float(input('Qual a massa do indivíduo (em quilogramas)? '))
IMC = m / (h * h)
print(IMC)
if IMC < 18.5:
    print('Abaixo do peso')
elif IMC <= 25:
    print('Peso ideal')
elif IMC <= 30:
    print('Sobrepeso')
elif IMC <= 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
