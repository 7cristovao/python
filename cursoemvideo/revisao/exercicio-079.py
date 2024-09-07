''' Crie um programa onde o usuário possa 
    digitar vários valores numéricos e 
    cadastre-os em uma lista. Caso o número
    já exista lá dentro, ele não será 
    adicionado. 
    No final, serão exibidos todos os 
    valores únicos digitados, em ordem 
    crescente. '''

numeros = []
while True:
    numero = int(input('Digite um número: '))
    resposta =  str(input('Quer continuar? ')).upper().strip()
    if resposta not in 'NnSs':
        print('Opção inválida! ')
    if resposta in 'Nn':
            numeros.append(numero)
            break
    if resposta in 'Ss':
        if numero in numeros:
            print('Este número já está na lista, portanto ele não será adicionado.')
            break
        else:
            numeros.append(numero)
print(f'A lista de números ordenada é {sorted(numeros)}')