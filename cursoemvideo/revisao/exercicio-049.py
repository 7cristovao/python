''' Refaça o desafio 009, mostrando a tabuada
    de um número que o usuário escolher, só 
    que agora utilizando um laço for. '''

num = int(input('Digite um número inteiro: '))
for c in range(0, 11):
    print(f'{num} x {c} = {num * c}')
print('Fim!')
