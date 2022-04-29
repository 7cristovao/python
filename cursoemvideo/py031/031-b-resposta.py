#!/usr/bin/env python3
# encoding: utf-8


# d : distância
d = float(input('Qual é a distância da sua viagem? '))   #  150 km      #210
print('Você está prestes a começar uma viagem de {}Km.'.format(d))      #até 200
# OPERADOR TERNÁRIO
# THEN           IF          ELSE
preço = d * 0.50 if d <= 200 else d * 0.45
print('E o preço de sua passagem será de R${:.2f}'.format(preço))   # 75.00  #94.50

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