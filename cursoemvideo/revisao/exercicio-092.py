''' Crie um programa que leia nome, ano de nascimento e
    carteira de trabalho e cadastre-os (com idade) em um
    dicionário se por acaso a CTPS for diferente de ZERO,
    o dicionário receberá também o ano de contratação e
    o salário. Calcule e acrescente, além da idade, com
    quantos anos a pessoa vai se aposentar.    '''

from datetime import datetime

pessoa = dict()
nome = str(input('Nome: '))
idade = str(input('Idade: '))
ctps = int(input('CTPS: '))
contratacao = int(input('Ano de contratação: '))
salario = int(input('Salário: '))
aposentadoria = contratacao + 35
pessoa = {'nome':nome, 'idade':idade, 'ctps':ctps, 'contratação':contratacao, 'salário':salario, 'aposentadoria':aposentadoria}
print(pessoa)
for k, v in pessoa.items():
    print(f'{k} {v}')