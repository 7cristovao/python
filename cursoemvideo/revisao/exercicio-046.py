''' Faça um programa que mostre na tela 
    uma contagem regressiva para o 
    estouro de fogos de artifício, indo
    de 10 até 0, com uma pausa de 
    segundo entre eles. '''

from time import sleep

print('Contagem regressiva para o estouro de fogos de artifício: ')
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('BUM! Fim do programa!')