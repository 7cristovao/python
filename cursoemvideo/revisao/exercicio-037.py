''' Escreva um programa 
    que leia um número
    inteiro qualquer e peça
    para o usuário escolher
    qual será a base de
    conversão. 
    
    - 1 para binário 
    - 2 para octal
    - 3 para hexadecimal '''

num = int(input('Digite um número inteiro: '))
opcao = int(input('Escolha uma opção: \n - 1 para binário \n - 2 para octal \n - 3 para hexadecimal \n\n '))

if opcao == 1:
    print(f'\n O número em binário é {bin(num)[2:]}')
elif opcao == 2:
    print(f'\n O número em octal é {oct(num)[2:]}')
elif opcao == 3:
    print(f'\n O número em hexadecimal é {hex(num)[2:]}')
else:
    print(f'Opção inválida!')