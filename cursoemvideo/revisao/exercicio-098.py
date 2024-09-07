''' Faça um programa que tenha uma
    função chamada contador(), que
    receba três parâmetros: início.
    fim e passo e realize a contagem.
    
    Seu programa tem que realizar três
    contagens através da função criada:
    
    a) De 1 até 10, de 1 em 1
    b) De 10 até 0, de 2 em 2
    c) Uma contagem personalizada. '''

def inserirLinha():
    print('-=' * 20)


def contador(inicio, fim, passo):
    inserirLinha()
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    c = 0
    for c in range(inicio, fim, passo):
        print(f'{c}', end=' ')
    print('FIM!')


def contadorPersonalizado(inicio, fim, passo):
    inserirLinha()
    print('Agora é sua vez de personalizar a contagem!')
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    inserirLinha()
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    c = 0
    if inicio < fim:
        for c in range(inicio, fim, passo):
            print(f'{c}', end=' ')
        print('FIM!')
    elif passo <= 0:
        if passo == 0:
            passo = -1
            for c in range(inicio, fim + passo, passo):
                print(f'{c}', end=' ')
            print('FIM!')
        else:
            for c in range(inicio, fim + passo, passo):
                print(f'{c}', end=' ')
            print('FIM!')
    else:
        passo = passo * (-1)
        for c in range(inicio, fim + passo, passo):
            print(f'{c}', end=' ')
        print('FIM!')


contador(1, 11, 1)
contador(10, -1, -2)
contadorPersonalizado(1, 1, 0)