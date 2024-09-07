''' Crie um programa que tenha uma tupla 
    única com nomes de produtos e seus 
    respectivos preços, na sequência. No
    final, mostre uma listagem de preços, 
    organizando os dados em forma tabular. '''

produtosEPrecos = ('Vassoura', 15,
                   'Rodo', 10,
                   'Pá', 10,
                   'Esfregão', 30,
                   'Esponja', 5,
                   'Detergente', 2,
                   'Limpador Multiuso', 7,
                   'Sabão em pedra', 1,
                   'Sabão Líquido', 15)
print('-'*41)
print('LISTAGEM DE PREÇOS')
print('-'*41)
for pos in range(0, len(produtosEPrecos)):
    if pos % 2 == 0:
        print(f'{produtosEPrecos[pos]:.<30}', end=' ')  # alinhado a esq
    else:
        print(f'R$ {produtosEPrecos[pos]:>7.2f} ')  # alinhado a dir
print('FIM')
