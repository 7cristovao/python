''' Crie um programa que leia vários números 
    inteiros pelo teclado. O programa só vai
    parar quando o usuário digitar o valor
    999, que é a condição de parada. No final
    mostre quantos números foram digitados e
    qual foi a soma entre eles 
    (desconsiderando o flag).'''

num = cont = soma = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    else:
        cont = cont + 1
        soma = soma + num
print(f'Foram digitados {cont} números e a soma entre eles é {soma}')