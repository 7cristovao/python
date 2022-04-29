#!/usr/bin/env python3


# Crie um programa que ANALISA o que foi digitado pelo usuário
# Verifique: 
# (1) Só tem espaços? 
# (2) É um número? 
# (3) É alfabético? 
# (4) É alfanumérico ? 
# (5) Está em maiúsculas? 
# (6) Está em minúsculas? 
# (7) Está capitularizada? #

profissao = input('Digite algo: ')
print('O tipo primitivo deste valor é', type(profissao))
print('Só tem espaços?', profissao.isspace())
print('É um número? ', profissao.isnumeric())
print('É alfabético? ', profissao.isalpha())
print('É alfanumérico? ', profissao.isalnum())
print('Está em maiúsculas ', profissao.islower())
print('Está em minúsculas ', profissao.isupper())
print('Está capitularizada? ', profissao.istitle())
