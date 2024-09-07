''' Crie um programa que simule 
    o funcionamento de um caixa
    eletrônico. No início, 
    pergunte ao usuário qual 
    será o valor a ser sacado 
    (número inteiro) e o programa
    vai informar quantas cédulas
    de cada valor serão entregues
    
    OBS: Considere que o caixa 
    possui cédulas de R$ 50, R$ 20,
    R$ 10 e R$ 1. '''


while True:
    saque = int(input('Qual o valor do saque: '))
    notasDe50 = saque // 50
    restoDasNotasDe50 = saque % 50
    notasDe20 = restoDasNotasDe50 // 20
    restoDasNotasDe20 = restoDasNotasDe50 % 20
    notasDe10 = restoDasNotasDe20 // 10
    restoDasNotasDe10 = restoDasNotasDe20 % 10
    notasDe1 = restoDasNotasDe10 // 1
    break
print(f'Serão entregues: ')
print(f'{notasDe50} notas de R$ 50,00')
print(f'{notasDe20} notas de R$ 20,00')
print(f'{notasDe10} notas de R$ 10,00')
print(f'{notasDe1} notas de R$ 1,00')