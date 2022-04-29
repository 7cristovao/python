#!/usr/bin/env python3
# encoding: utf-8


if velocidade >_
velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80 km/h')
    multa = (velocidade-80) * 7
    print('Voce deve pagar uma multa de R${:.2f}!'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança!')

# OBSERVAÇÃO: CEDILHA NÃO FUNCIONA SEM ATRIBUIR A CODIFICAÇÃO UTF-8