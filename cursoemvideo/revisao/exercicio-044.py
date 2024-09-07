''' Elabore um programa que calcule
    o valor a ser pago por um 
    produto, considerando o seu
    preço normal e condição de
    pagamento:
    - à vista dinheiro/cheque: 10% de desconto
    - à vista no cartão: 5% de desconto
    - em até 2x no cartão: preço normal
    - 3x ou mais no cartão: 20% de juros '''

precoNormal = float(input('Digite o preço normal: '))
print('1 - à vista no dinheiro/cheque: 10%' ' de desconto')
print('2 - à vista no cartão: 5%' ' de desconto')
print('3 - em até 2x no cartão: preço normal')
print('4 - 3x ou mais no cartão: 20%'' de juros')
condicaoDePagamento = int(input('Escolha a condição de pagamento: '))

if condicaoDePagamento == 1:
    print(f'Valor a ser pago = {precoNormal * 0.90}')
elif condicaoDePagamento == 2:
    print(f'Valor a ser pago = {precoNormal * 0.95}')
elif condicaoDePagamento == 3:
    print(f'Valor a ser pago = {precoNormal}')
elif condicaoDePagamento == 4:
    print(f'Valor a ser pago = {precoNormal * 1.20}')
else:
    print(f'Condição inválida!')
    