''' Crie um programa onde o usuário possa digitar 
    cinco valores numéricos e cadastre-os em uma 
    lista, já na posição correta de inserção
    (sem usar o sort()). 
    
    No final, mostra a lista ordenada na tela. '''

menor = 0
numeros = []
for posicao in range(0, 5):
    numero = int(input('Digite um número: '))
    if posicao == 0 or numero > numeros[-1]:
        numeros.append(numero)
        print('Adicionado ao final da lista...')
    else:
        posicao = 0
        while posicao < len(numeros):
            if numero <= numeros[posicao]:
                numeros.insert(posicao, numero)
                print(f'Adicionado na posição {posicao} da lista...')
                break
            posicao = posicao + 1
print(f'Os valores digitados em ordem foram {numeros}')
print('FIM')