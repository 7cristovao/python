# 0-1-1-2-3-5-8

# Crie um programa que leia VÁRIOS NÚMEROS
# inteiros pelo teclado. O programa só vai parar quando o 
# usuário digitar o valor 999,  que é a CONDIÇÃO DA PARADA
# No final mostre QUANTOS NÚMEROS foram digitados e qual foi
# a soma entre eles (DESCONSIDERANDO O FLAG [esse 999])

núm = cont = soma = 0
núm = int(input('Digite um número [999 para parar]: '))
while núm != 999:
    soma += núm    
    cont += 1
    núm = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))

