''' Escreva um programa que 
    pergunte a quantidade 
    de KM percorridos por 
    um carro alugado e a 
    quantidade de dias pelos 
    quais ele foi alugado. 
    Calcule o preço a pagar,
    sabendo que o carro custa
    R$ 60 por dia e R$ 0,15
    por Km rodado. '''

distancia = int(input('Qual a quantidade de quilomêtros percorridos pelo carro alugado? '))
quantidadeDeDiarias = int(input('Quantas diárias? '))
total = distancia * 0.15 + 60.0 * quantidadeDeDiarias
print(f'O preço a pagar é de {total:.2f}')
