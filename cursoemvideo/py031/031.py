#!/usr/bin/env python3
# encoding: utf-8


# Crie um código que questione a distância de uma viagem em km 
# Calcule o preço da passagem, cobrando R$ 50,50 por Km para viagens de até 200Km
# a R$0.45 para viagens mais longas #

# d : distância
d = float(input('Qual é a distância da sua viagem? '))   #  150 km      #210
if d <= 200:
    print('Você está prestes a começar uma viagem de {}Km.'.format(d))      #até 200
    print('E o preço de sua passagem será de R${:.2f}'.format(d * 0.5))   # 75.00  #94.50
else:
    print('Você está prestes a começar uma viagem de {}Km.'.format(d))      #até 200
    print('E o preço de sua passagem será de R${:.2f}'.format(d * 0.45))   # 75.00  #94.50





#     150 = 75
#     1 = x
#      
#     150x = 75
#        x = 75/150
#        x = 1/2
# 
#     210x = 94.50
#        x = 94.50 / 210
#        x = 0.45  
#    

