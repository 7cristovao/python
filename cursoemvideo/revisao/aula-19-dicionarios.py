dados = dict()
dados = {'nome':'Pedro', 'idade':25}
print(dados['nome'])
print(dados['idade'])
dados['sexo'] = 'M'

# elimina pela chave idade
del dados['idade']

filme = {
    'titulo':'Star Wars',
    'ano':1977,
    'diretor':'George Lucas'
}

# imprime na tela os valores de um dicionário
print(filme.values())

# imprime na tela as chaves de um dicionário
print(filme.keys())

# exibe as chaves e os valores
print(filme.items())

# imprime na tela as chaves e os valores de um laço em um dicionário
for k, v in filme.items():
    print(f'O {k} é {v}')

# exemplo de utilização de um dicionário dentro de uma lista
locadora = [{'titulo':'Star Wars','ano':1977,'diretor':'George Lucas'},{'titulo':'Avengers','ano':2012,'diretor':'Joss Whedon'},{'titulo':'Matrix','ano':1999,'diretor':'Wachowski'}]
print(locadora[0]['ano'])
print(locadora[2]['titulo'])

# outro exemplo de dicionário
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}

# exibe num print formatado chaves e valores de um dicionário
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')

# exibe apenas as chaves
for k in pessoas.keys():
    print(k)

# exibe apenas os valores
for k in pessoas.values():
    print(k)

# exibe chaves e valores
for k in pessoas.items():
    print(f'{k} = {v}')

# sobrescrevendo um item
pessoas['nome'] = 'Leandro'

# adicionando um item
pessoas['peso'] = 98.5

# criando um dic dentro de uma lista
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[1]['sigla'])

# como fazer uma cópia de um elemento sem fazer fatiamento
estados = dict()
brasil = list()
for c in range(0, 3):
    estados['uf'] = str(input('Unidade Federativa: '))
    estados['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estados.copy())
print(brasil)

# para melhorar mostrando que cada estado é um dicionario
for e in brasil:
    print(e)

# mostrar personalizado
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')

# outro exemplo mostrando só valores
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()