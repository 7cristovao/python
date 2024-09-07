''' Crie um programa que vai ler vários números 
    e colocar em uma lista. 
    
    Depois disso, crie duas listas extras que vão
    conter apenas os valores pares e os valores
    ímpares digitados, respectivamente. 
    
    Ao final, mostre o conteúdo das três listas geradas. '''

lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    resposta = str(input('Deseja continuar? '))
    if resposta not in 'SsNn':
        continue
    elif resposta in 'Nn':
        break
    else:
        continue
print(f'Os valores da lista são {lista}')
listaPares = []
listaImpares = []
for c in lista:
    if c % 2 == 0:
        listaPares.append(c)
    else:
        listaImpares.append(c)
print(f'Os valores pares da lista são {listaPares}')
print(f'Os valores ímpares da lista são {listaImpares}')
print('FIM')