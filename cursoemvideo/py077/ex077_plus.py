#!/usr/bin/env python3


# Crie um programa que tenha uma TUPLA com VARIAS PALAVRAS
# (nao usar acentos).
# Depois disso, voce deve mostrar, para cada palavra, quais sao as 
# suas VOGAIS.

palavras = (
'APRENDER',
'PROGRAMAR',
'LINGUAGEM',
'PYTHON',
'CURSO',
'GRATIS',
'ESTUDAR',
'PRATICAR',
'TRABALHAR',
'MERCADO',
'PROGRAMADOR',
'FUTURO'
)

palavra = palavras[0].lower()
print(palavra)
separaletras = ' '.join(str(palavra))
print(separaletras)
separa = separaletras.split()
print(separa)
print(str(separa).replace('a','1'))
print(str(separa).replace('e','1'))
print(str(separa).replace('i','1'))
print(str(separa).replace('o','1'))
print(str(separa).replace('u','1'))

#print(palavras.index('a'))

#x = 0
#y = 0
#z = 0
#w = 0
#for n in palavras:
    
#print('Na palavra {} temos {} {} {}'.format(x, y, z, w)) 
