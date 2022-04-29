#!/usr/bin/env python3
# encoding: utf-8

# Salário de um func e o valor do aumento, abaixo de 1250 cresce o salario em 15%
# acima salario aumenta 10%

# sqn : salário quantia nova
salário = input(str('Qual é o salário do funcionário? R$'))  #  900.00    9000.00
salário = float(salário)
if salário > float(1250):
    sqn = salário * 1.10
else:
    sqn = salário * 1.15
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário,sqn))  # 1.15*1035.00
                                                                           # 1.10*9900.00
