#!/usr/bin/env python3


# Crie um código que mostre se o nome digitado tem Silva

nome = str(input('Qual é o seu nome completo? ')).lower().strip()
print('Seu nome tem Silva? {} '.format(nome.find('silva') == False))