''' Faça um programa que leia
    um ano qualquer e mostre
    se ele é BISSEXTO. '''

ano = int(input('Digite o ano: '))
resto = ano % 4
if resto == 0:
    print('Este ano é bissexto.')
else:
    print('Este ano NÃO é bissexto.')