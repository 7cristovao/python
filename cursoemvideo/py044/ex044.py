#!/usr/bin/env python3


# Elabore um programa que calcule o valor a ser pago
# por um produto considerando o seu
# PREÇO NORMAL e CONDIÇÃO DE PAGAMENTO:

# (1) À vista DINHEIRO/CHEQUE: 10% de desconto
# (2) À vista no CARTÃO: 5% de desconto
# (3) em até 2X NO CARTÃO: preço normal
# (4) 3X OU MAIS no cartão: 20% de juros #

pgto = int(input("Forma de pagamento: "
"\nOpção 1: dinheiro à vista OU cheque, 10% De desconto"
"\nOpção 2: parcela ÚNICA no cartão de crédito, 5% De desconto"
"\nOpção 3: em até 2 vezes no cartão de crédito, preço normal"
"\nOpção 4: em 3 vezes ou mais no cartão, 20% De juros\n"))
valor = float(input('Digite o valor do produto em R$: '))
if pgto == 1:
    print('O valor a ser pago é de R$ {:.2f}'.format(valor * 0.9))
elif pgto == 2:
    print('O valor a ser pago é de R$ {:.2f}'.format(valor * 0.95))
elif pgto == 3:
    print('O valor a ser pago é de R$ {:.2f}'.format(valor))
elif pgto == 4:
    print('O valor a ser pago é de R$ {:.2f}'.format(valor * 1.2))
else:
    print('Houve algum problema na digitação do valor, digite novamente')
