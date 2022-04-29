#!/usr/bin/env python3


# Crie um programa que lê uma FRASE qualquer e diga se ela é um
# PALÍNDROMO, desconsiderando os espaços.

# Ex. 
# APOS A SOPA 
# A SACADA DA CASA 
# A TORRE DA DERROTA 
# O LOBO AMA O BOLO 
# ANOTARAM A DATA DA MARATONA #


# (1) ler a frase
# (2) tirar os espaços
# (3) colocar em maiuscula

# (4) separa cada palavra da frase
# (5) junta as palavras com ''
# (6) string que le de tras pra frente vazia no inicio

# (7) for para varrer a stringa da ultima ate a primeira

frase = str(input('Digite uma frase: ')).strip().upper()  #  (1) (2) (3)
palavras = frase.split() #  (4)
junto = ''.join(palavras)  #  (5)
inverso = ''  #  (6)
for letra in range(len(junto) - 1, -1, -1)
    inverso += junto[letra]
if inverso == junto:
    print('É palindromo')
else:
    print('Não é um palindromo')

