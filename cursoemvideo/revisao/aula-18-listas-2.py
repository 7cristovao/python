teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()

# Adiciona uma lista dentro de uma lista vazia fazendo uma cópia
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

# exemplo de uma lista composta dentro de outra lista
# nomes nas posições 1 e idades nas posições 2
galera1 = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]

# exibe o item 1 dentro da posição 2
print(galera1[2][1])

# exibe apenas os nomes
for p in galera1:
    print(p[0])

# exibe apenas as idades
for p in galera1:
    print(p[1])

# exibindo os dois itens de uma lista dentro de outra
for p in galera1:
    print(f'{p[0]} tem {p[1]} anos de idade.')

galera2 = list()

# cria lista secundária para pegar temporariamente os dados dessa lista
dado = list()

# pega dados de 5 pessoas
for c in range(0, 3):
    # lê o nome
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    
    # pega o dado e joga dentro da lista galera 
    galera2.append(dado[:])
    
    # exclui dado
    dado.clear()

print(galera2)

# mostra só as pessoas que tem mais de 21 anos
totmai = totmen = 0
for p in galera2:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade')