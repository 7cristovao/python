#!/usr/bin/env python3


# Desenvolva um código que mostre se o nome digitado começa ou não 
# com a palavra santo

x = str(input('Em que cidade você nasceu? ')).strip()
xa = x[0:5].upper()
print(xa == 'SANTO')
