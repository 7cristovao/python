''' Faça um programa que leia 5 valores 
    numéricos e guarde-os em uma lista. 
    
    No final, mostre qual foi o maior e 
    o menor valor digitado e as suas 
    respectivas posições na lista. '''

listaNumeros = []
maior = 0
menor = 0
for posicao in range(0, 5):
    listaNumeros.append(int(input('Digite um número: ')))
    if posicao == 0:
        maior = menor = listaNumeros[posicao]
    else:
        if listaNumeros[posicao] > maior:
            maior = listaNumeros[posicao]
        if listaNumeros[posicao] < menor:
            menor = listaNumeros[posicao]
print(f'Você digitou os valores {listaNumeros}')
print(f'O maior valor digitado foi {maior} na(s) posição(ões) ')
for chave, valor in enumerate(listaNumeros):
    if valor == maior:
        print(f'{chave}...', end='')
print()
print(f'O menor valor digitado foi {menor} na(s) posição(ões) ')
for chave, valor in enumerate(listaNumeros):
    if valor == menor:
        print(f'{chave}...', end='')
print()
    