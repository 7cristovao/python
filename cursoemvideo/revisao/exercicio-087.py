''' Aprimore o desafio, mostrando no final: 
    
    A) A soma de todos os valores pares digitados.
    
    B) A soma dos valores da terceira coluna.

    C) O maior valor da segunda linha.
    
    '''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPares = 0
somaJ = 0
maior = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite o valor para [{i}, {j}]: '))
        if matriz[i][j] % 2 == 0:
            somaPares = somaPares + matriz[i][j]
        if matriz[i][2]:
            somaJ = somaJ + matriz[i][2]
if matriz[1][0] > matriz[1][1] and matriz[1][0] > matriz[1][2]:
    maior = matriz[1][0]
elif matriz[1][1] > matriz[1][0] and matriz[1][1] > matriz[1][2]:
    maior = matriz[1][1]
elif matriz[1][2] > matriz[1][0] and matriz[1][2] > matriz[1][1]:
    maior = matriz[1][2]
elif matriz[1][0] == matriz[1][1] == matriz[1][2]:
    maior = matriz[1][0]
elif matriz[1][0] == matriz[1][1] > matriz[1][2]:
    maior = matriz[1][0]
elif matriz[1][0] == matriz[1][2] > matriz[1][1]:
    maior = matriz[1][0]
elif matriz[1][1] == matriz[1][2] > matriz[1][0]:
    maior = matriz[1][1]
else:
    print('Opção inválida')
print(f'A soma de todos os valores pares digitados é {somaPares}')
print(f'A soma dos valores da terceira coluna é {somaJ}')
print(f'O maior valor da segunda linha é {maior}')
print(f'{matriz[0]} \n {matriz[1]} \n {matriz[2]}')
print('FIM')