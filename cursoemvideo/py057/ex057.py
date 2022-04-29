#!/usr/bin/env python3


# 57

# Faça um programa que lê o sexo de uma pessoa, mas 
# só aceite os valores ' M " ou ' F '.
# Caso esteja errado, peça a digitação novamente
# até ter um valor correto

sexo = 0
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Sexo M ou F: '))
print('fim')

