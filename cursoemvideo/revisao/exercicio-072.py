''' Crie um programa que tenha uma tupla totalmente 
    preenchida com uma contagem por extenso, de zero 
    até vinte. 
    
    Seu programa deverá ler um número pelo teclado 
    (entre 0 e 20) e mostrá-lo por extenso. '''

numerosPorExtenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

numero = int(input('Digite um número para vê-lo escrito por extenso: '))
print(f'Este número escrito por extenso é {numerosPorExtenso[numero]}')
