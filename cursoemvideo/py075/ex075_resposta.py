#!usr/bin/env python3


# Desenvolva um programa que leia QUATRO VALORES pelo 
# TECLADO  e guarde-os em uma TUPLA. No final mostre:

# A) Quantas vezes apareceu o valor 9

# B) Em que posição foi digitado o primeiro valor 3.

# C) Quais foram os números PARES


num = (int(input('Dig um num.:')), int(input('Dig um num.:')), int(input('Dig
um num.:')), int(input('Dig um num.:')), int(input('Dig um num.:')))  # (1)
print('Voce digitou os valores {}'.format(num))  # (1)
print('O valor 9 apareceu {} vezes'.format(num.count(9)))  # (1)
if 3 in num:  # (3)
    print('O valor 3 apareceu na posicao {}'.format(num.index(3)+1))  # (1)
else:  # (3)
    print('O valor 3 nao foi digitado em nenhuma posicao')  # (3)
print('Os valores pares digitados foram ', end=' ')   # (3)
for n in num:  # (2)
    if n % 2 == 0:   # (2)
        print(n, end=' ')  # (2)

# (3) resolve o erro da aplicacao por nao se ter digitado o valor
