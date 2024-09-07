lanche = ('Hamburguer','Suco','Pizza','Pudim')

# Iterar cada item da tupla
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba')

# Iterando a tupla
for cont in range(0, len(lanche)):
    print(lanche[cont])
print('Comi pra caramba')

# Iterando a tupla mostrando apenas o índice
for cont in range(0, len(lanche)):
    print(cont)
print('Comi pra caramba')

# Iterando a tupla exibindo frase personalizada
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print('Comi pra caramba')

# Iterando a tupla exibindo frase personalizada e a posição do índice
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi pra caramba')

# Iterando a tupla exibindo frase personalizada e a posição do índice
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba')


lanches = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# Exibir a tupla em ordem alfabética
print(sorted(lanches))

# Juntar/Concatenar duas tuplas em uma
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(len(c))
print(c.count(5)) # conta quantas vezes o 5 aparece na tupla
print(c.index(8)) # exibe o valor que está na posição 8
print(c.index(5, 1)) # exibe o valor que está na posição 8, ignorando a posição 0, começando da posição 1

# Tupla com tipos diferentes de dados
pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)

# Linha de código para apagar a tupla
del(pessoa)
print(pessoa)

# OBSERVAÇÃO: AS TUPLAS SÃO IMUTÁVEIS
# Não é possível apagar itens de uma tupla
del(pessoa[0])
print(pessoa)