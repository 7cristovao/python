''' Escreva um programa para aprovar
    o empréstimo bancário para a 
    compra de uma casa. Pergunte o 
    valor da casa, o salário do 
    comprador e em quantos anos ele
    vai pagar.
    A prestação mensal, não pode 
    exceder 30% do salário ou então
    o empréstimo será negado. '''

valorDaCasa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salário: '))
anosParaPagamento = float(input('Digite em quantos anos pretende pagar: '))
mesesParaPagamento = anosParaPagamento * 12 
parcelaDaCasa = valorDaCasa / mesesParaPagamento
print('\n')
print(f'30% do salario = {0.3 * salario}')
print(f'quantidade Parcelas = {mesesParaPagamento:.0f}')
print(f'parcela = {parcelaDaCasa:.2f}')
print('\n')

if parcelaDaCasa > 0.3 * salario:
    print('O empréstimo foi negado.')
else:
    print('O empréstimo foi aprovado.')