''' Crie um programa que tenha uma tupla com várias palavras 
    (não usar acentos). Depois disso, você deve mostrar, para
    cada palavra, quais são suas vogais. '''

palavras = ('abacaxi', 'manga', 'cartola', 'calculadora', 'moeda', 'barro')
for pos in range(0, len(palavras)):
    print(f'\nNa palavra {palavras[pos]} temos as vogais ')
    for letra in palavras[pos]:
        if letra in 'aeiou':
            print(f'{letra}', end='') 
print('\n\nFIM')

