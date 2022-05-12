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

for p in palavras:  #  (1)
    print('\nNa palavra {} temos '.format(p), end='') #  (2)
    for letra in p:  #  (3)
       if letra.lower() in 'aeiou':  #  (4)
           print(letra.lower(), end=' ')  #  (5)
print('\n')

#  p : palavra

#  (1) pra cada p a gente vai ter que fazer um laco
#  (2) para cada uma das palavras, a p. APRENDER eh uma lista de letras
#  (3) pra cada letra em p posso verificar
#  (4) se a letra estiver em 'aeiou',
#  (5) escreve a letra
