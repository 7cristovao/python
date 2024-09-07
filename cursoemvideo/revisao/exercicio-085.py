''' Crie um programa onde o usuáŕio possa
    digitar sete valores numéricos e
    cadastre-os em uma lista única que
    mantenha separados os valores pares e
    ímpares. No final, mostre os valores
    pares e ímpares em ordem crescente. '''

num = [[],[]]
valor = 0
for c in range(0,7):
    valor = int(input(f'Digite o valor {c+1}: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'Pares = {num[0]}')
print(f'Ímpares = {num[1]}')
print('FIM')