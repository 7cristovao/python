# Crie um programa que lê VÁRIOS NÚMEROS inteiros
# pelo teclado. No final da execução, mostre a 
# MÉDIA ENTRE TODOS os valores e qual foi o MAIOR
# e o MENOR valores lidos. O programa deve 
# perguntar ao usuário se ele quer ou não CONTINUAR
# a digitar valores

resp = 'S'
soma = quant = média = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
média = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, média))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))
print('acabou')
