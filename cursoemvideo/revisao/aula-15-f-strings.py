nome = 'José'
idade = 33
# python 3.6+
print(f'O {nome} tem {idade} anos.')

# python 3
print('O {} tem {} anos.'.format(nome, idade))

# python 2
print('O %s tem %d anos.' % (nome, idade))

# nome aparecer com 20 espaços
print(f'{nome:20}')

# centralizar
print(f'{nome:^20}')

# complementar
print(f'{nome:-^20}')

# alinhado a direita
print(f'{nome:->20}')

# alinhado a esquerda
print(f'{nome:-<20}')