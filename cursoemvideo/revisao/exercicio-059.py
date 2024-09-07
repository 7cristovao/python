''' Crie um programa que leia dois valores 
    e mostre um menu na tela: 
    
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa

    Seu programa deverá realizar a operação
    solicitada em cada caso.
    '''

soma = 0
opcao = -1
maior = 0
num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: ')) 
while opcao != 5:
    print(''' 
          
          Você deseja:

          [1] somar 
          [2] multiplicar
          [3] maior
          [4] novos números
          [5] sair do programa
          ''')
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        soma = num1 + num2
        print(f'A soma de {num1} + {num2} é {soma}')
    elif opcao == 2:
        produto = num1 * num2
        print(f'A multiplicação de {num1} x {num2} é de {num1 * num2}')
    elif opcao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        if num1 == num2:
            print(f'Os números {num1} e {num2} são iguais')
        else:
            print(f'O maior número entre {num1} e {num2} é {maior}')
    elif opcao == 4:
        print('Digite os números novamente:')
        num1 = int(input('Digite um valor: '))
        num2 = int(input('Digite outro valor: ')) 
    elif opcao == 5:
        print(f'Saindo do programa...')
    else:
        print(f'Opção inválida! Tente novamente')
print('Fim do programa')