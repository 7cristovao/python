#!/usr/bin/env python3


# Faça um algoritmo que lê o salário de um funcionário e mostra seu 
# novo salário com 15% de aumento
salário = float(input('Qual é o salário do funcionário? R$'))
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salário, salário * 1.15)) 
