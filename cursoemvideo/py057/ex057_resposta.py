#!/usr/bin/env python3


sexo = str(input('Informe seu sexo: ')).strip().upper()[0]
while sexo not in 'MmFm':
    sexo = str(input('Dados inválidos. Por favor informe seu sexo: '))
print('Sexo {} registado com sucesso'.format(sexo))