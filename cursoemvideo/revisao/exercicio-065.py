''' Crie um programa que leia vários números inteiros 
    pelo teclado. No final da execução, mostre a média
    entre todos os valores e qual foi o maior e o 
    menor valores lidos. O programa deve perguntar 
    ao usuário se ele quer ou não continuar a digitar
    valores. '''

num = 0
respostaUsuario = 'S'
soma = 0
cont = 0
while respostaUsuario in 'Ss':
    num = int(input('Digite um número: '))
    soma = soma + num
    cont = cont + 1
    if cont == 1:
        maior = menor = num
    else: 
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    respostaUsuario = str(input('Você quer continuar a digitar valores? (S/N): ')).upper()
print(f'A média dos valores é de {soma/cont}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
print(cont)