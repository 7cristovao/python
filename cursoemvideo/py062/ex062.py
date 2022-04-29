#!/usr/bin/env python3
#   
# 
# Melhore o exercício 61, perguntando 
# para o usuário se ele quer mostrar
# mais alguns termos. O programa encerra
# quando ele disser que quer mostrar
# ZERO TERMOS

a_0 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
i = int(input('Digite a quantidade de termos que você quer exibir na PA: '))
cont = -1  # i
while cont < i:        
     cont += 1
     print ('O {}º termo da PA é igual a {} '.format(cont, a_0 + (r * (cont))))
print('fim\n')
