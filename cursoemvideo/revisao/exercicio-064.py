''' Crie um programa que leia vários números 
    inteiros pelo teclado. O programa só vai
    parar quando o usuário digitar o valor 
    999, que é a condição de parada. No final,
    mostre quantos números foram digitados e 
    qual foi a soma entre eles. 
    (desconsiderando o flag). '''

cont = 0
soma = 0
num = 0
print('999 para sair')
while num != 999:
    num = int(input('Digite um número: '))
    cont = cont + 1
    soma = soma + num
print(f'Foram digitados {cont - 1} números.')
print(f'A soma entre os números é de {soma - 999}.')