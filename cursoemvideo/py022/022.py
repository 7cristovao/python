#!/usr/bin/env python3


#ANÁLISE
#len(frase)
#frase.count('o',inicial,final) 
#frase.count('o',inicial,final)
#frase.find('o')
#'palavra' in frase
#frase.replace('o','e')
#frase.upper()
#frase.lower()
#frase.capitalize()
#frase.title()
#frase.strip()
#frase.rstrip()
#frase.lstrip()
#frase.split

#DIVISÃO
#frase.split()
#lista0 lista1
#012345 012345
#
#JUNTA
#'-'.join(frase)
#


# Crie um programa que lê o nome completo de uma pessoa e mostre: 
# (1) O nome com todas as letras maiúsculas 
# (2) O nome com todas as letras minúsculas
# (3) Quantas letras ao todo (sem considerar espaços) 
# (4) Quantas letras tem o primeiro nome #

nome = str(input('Digite seu nome completo: '))
print('Analisando seu nome...')
NOMÃO = nome.upper()
print('Seu nome em maiúsculas é', format(NOMÃO))
nominho = nome.lower()
print('Seu nome em minúsculas é', format(nominho))
print('Seu nome tem ao todo ' + str(len(nome)) + ' letras')
fatia = nome.split()
#print(fatia)
separa = fatia[0]
#print(separa)
print('Seu primeiro nome é ' + str(separa) + ' e ele tem ' + str(len(separa)) + ' letras')
