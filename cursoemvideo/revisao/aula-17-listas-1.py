# atribui uma lista de números à variável
num = [2, 5, 9, 1]

# modifica o item da posição atribuindo um novo valor
num[2] = 3

# atribui um número ao final da lista
num.append(7)

# coloca lista em ordem crescente
num.sort()

# coloca lista em ordem decrescente
num.sort(reverse=True)

# insere valor 2 na posição zero
num.insert(2, 0)

# remove valor da posição 2
num.pop(2)

# remove valor da última posição da lista
num.pop()

# procura do início da lista a primeira ocorrência da lista e elimina
num.remove(5)

if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)

# exibe a quantidade de elementos de uma lista
print(f'A quantidade de elementos desta lista é de {len(num)}')

# cria uma lista vazia
valores = list()

# atribui valores à lista
valores.append(5)
valores.append(9)
valores.append(4)

# para mostrar personalizado os valores de uma lista na mesma linha
for valor in valores:
    print(f'{valor}...', end='')

print('\n')

# para mostrar os índices e os valores 
for chave, valor in enumerate(valores):
    print(f'Na posição {chave} encontrei o valor {valor}!')
print('Cheguei ao final da lista.')

# ler valores pelo teclado e colocá-los em uma lista
numeros = []
for cont in range(0, 5):
    numeros.append(int(input('Digite um valor: ')))

# criar uma ligação de listas
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

# criar uma cópia de listas

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')