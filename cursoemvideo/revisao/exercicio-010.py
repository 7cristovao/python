''' Crie um programa 
    que leia quanto 
    dinheiro uma pessoa
    tem na carteira 
    e mostre quantos 
    Dólares ela pode
    comprar.

    Considere US$ 1,00 = R$ 3,27 '''

dinheiroNaCarteira = float(input('Digite quanto dinheiro você tem na carteira: '))
print(f'Você tem R${dinheiroNaCarteira}. Você pode comprar US$ {dinheiroNaCarteira / 3.27:.2f}.')
