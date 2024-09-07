''' Crie um programa que crie uma matriz de 
    dimensão 3x3 e preencha com valores lidos
    pelo teclado. 
    
       _ _ _
    0 |_|_|_|
    1 |_|_|_|
    2 |_|_|_|
       0 1 2
    
    No final, mostre a matriz na tela, com 
    a formatação correta. '''


# matriz = [[11, 12, 13],[21, 22, 23],[31, 32, 33]]
# print(matriz)
# print(f'{matriz[0]}\n{matriz[1]}\n{matriz[2]}')
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite um número para [{i}, {j}]: '))
print(f'{matriz[0]}\n{matriz[1]}\n{matriz[2]}')
print('FIM')


    