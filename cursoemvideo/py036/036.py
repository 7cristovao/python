#!/usr/bin/env python3


from math import sqrt
sqrt(2)
# Crie um código que aprove o emprestimo bancario
# para a compra se uma casa. O programa vai perguntar o VALOR DA CASA.
# o SALÁRIO DO COMPRADOR  e em QUANTOS ANOS  ele vai pagar
#
# Calcule o valor da prestação mensal sabendo que ela
# não pode exceder 30% do salário ou então NEGO o empréstimo#

# oz : salário do comprador
# os : valor da casa
# oa : quantos anos para o pagamento
# om : quantidade de meses

os = float(input('Qual o valor da casa? '))
oz = float(input('Salário do comprador? '))
oa = float(input('Quantos anos para o pagamento? '))
om = oa * 12
osom = os / om
if osom > (0.30 * oz):
    print('NEGO')
else:
    print('O valor da prestação mensal é: R$ {}'.format(osom))
