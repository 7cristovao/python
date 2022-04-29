#!/usr/bin/env python3
# encoding: utf-8


# Escreva um programa que lê a velocidade de um carro 
# (1) Se ele ultrapassar 80 km/h mostre uma mensagem 
# dizendo que ele foi multado 
# 
# (2) A multa vai custar R$ 7,00 por cada km acima do limite 

# velocidade : v
v = int(input('Qual a velocidade atual do carro? '))
print(v)
if v > 80:
    print('Voce deve pagar uma multa de R$280.00!')
else:
    print('Tenha um bom dia! Dirija com segurança!')

# OBSERVAÇÃO: CEDILHA NÃO FUNCIONA SEM ATRIBUIR A CODIFICAÇÃO UTF-8