#!usr/bin/env python3


# TUPLA
# Crie um programa que tenha uma TUPLA totalmente preenchida com uma
# contagem por extenso, de ZERO  até VINTE.

# Seu programa deverá ler um número pelo teclado
# ENTRE ZERO E VINTE e mostrá-lo por EXTENSO

# num : numero

cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um numero entre 0 e 20: ')
    if 0 <= n <= 20:
        break
    print('Tente novamente. '.format(num, end=''))
print('Voce digitou o numero {}'.format(cont, end=''))
 
