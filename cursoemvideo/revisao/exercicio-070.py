''' Crie um programa que leia o nome e o 
    preço de vários produtos. O programa 
    deverá perguntar se o usuário vai 
    continuar. No final, mostre:
    
    A) Qual é o total gasto na compra.
    B) Quantos produtos custam mais de R$ 1000.
    C) Qual é o nome do produto mais barato. '''

somaCompra = 0
contProdutosMaioresQueMil = 0
menor = 0
cont = 0
produtoMaisBarato = ''
while True:
    produto = str(input('Digite o nome de um produto: '))
    preco = float(input('Digite o preço: '))
    cont = cont + 1
    somaCompra = somaCompra + preco
    if preco > 1000:
        contProdutosMaioresQueMil = contProdutosMaioresQueMil + 1
    if cont == 1:
        menor = preco
        produtoMaisBarato = produto
    else:
        if preco < menor:
            menor = preco
            produtoMaisBarato = produto
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if resposta == 'N':
        break
print(f'O total da compra foi de R$ {somaCompra:.2f}')
print(f'{contProdutosMaioresQueMil} produto(s) custa(m) mais de R$ 1000')
print(f'O produto mais barato foi {produtoMaisBarato} que custa R$ {menor:.2f}')
print('Fim do programa')
        