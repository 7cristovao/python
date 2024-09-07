''' Crie um programa que tenha uma função fatorial()
    que receba dois parâmetros: o primeiro que indique
    o número a calcular e o outro chamado show, que 
    será um valor lógico (opcional) indicando se será
    mostrado ou não na tela o processo de cálculo do 
    fatorial. '''

def fatorial(num1, show):
    """
    → Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do Fatorial de um número n.
    """
    fat = 1
    for c in range(num1, 0, -1):
        fat = fat * c
        if show == True:
            print(f'{c} x ', end='')
        else:
            print(end='')
    print(fat)

fatorial(3, show=False)
help(fatorial)