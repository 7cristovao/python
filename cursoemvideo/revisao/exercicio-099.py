''' Faça um programa que tenha uma 
    função chamada maior(), que 
    receba vários parâmetros com 
    valores inteiros. 
    
    Seu programa tem que analisar
    todos os valores e dizer qual 
    deles é o maior. '''

def maior(* num):
    print('-=' * 20)
    print('Analisando os valores passados...')
    if not num:
        return print('Foram informados 0 valores ao todo.\nO maior valor informado foi 0')
    else:
        for valor in num:
            print(f'{valor} ', end='')
        print('Foram informados 6 valores ao todo.')
        print(f'O maior valor informado foi {max(num)}.')
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()