#!/usr/bin/env python3


nome = str(input('Qual é o seu nome completo? ')).strip()
print('Seu nome tem Silva? {} '.format('silva' in nome.lower()))