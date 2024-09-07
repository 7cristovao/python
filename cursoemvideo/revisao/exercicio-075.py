''' Desenvolva um programa que leia quatro valores
    pelo teclado e guarde-os em uma tupla. No final
    mostre:
    
    A) Quantas vezes apareceu o valor 9. 
    B) Em que posição foi digitado o primeiro valor 3
    C) Quais foram os números pares. '''

c = 0
num = (int(input('Digite um número: ')), 
       int(input('Digite um número: ')), 
       int(input('Digite um número: ')), 
       int(input('Digite um número: ')))
print(f'O valor 9 apareceu {num.count(9)} vezes.')
print(f'O primeiro valor 3 foi digitado na posição {num.index(3)+1}')
print(f'Os números pares foram: ')
for c in num:
    if c % 2 == 0:
        print(c, end=' \n') 