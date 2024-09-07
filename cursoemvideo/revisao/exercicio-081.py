''' Crie um programa que vai ler vários números 
    e colocar em uma lista.
    
    Depois disso, mostre:
    
    A) Quantos números foram digitados.
    
    B) A lista de valores, ordenada de forma
    decrescente.
    
    C) Se o valor 5 foi digitado e está ou não
    na lista. '''

lista = []
cont = 0
while True:
    lista.append(int(input('Digite um número: ')))
    resposta = str(input('Deseja continuar (S/N)? '))
    if resposta not in 'SsNn':
        continue
    elif resposta in 'Nn':
        cont = cont + 1
        break
    else:
        cont = cont + 1
        continue
print(f'Foram digitado(s) {cont} número(s)')
lista.sort(reverse=True)
print(f'Os números em ordem decrescente são {lista}')
if 5 in lista:
    print(f'O número 5 foi digitado e está na lista')
else:
    print(f'O número 5 não foi digitado e não está na lista')