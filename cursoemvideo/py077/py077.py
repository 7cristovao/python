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

palavra = palavras.split()
for palavra in palavras:
    if 'AEIOU' in palavras:
        print('{} tem as vogais {}'.format(palavras, palavra))
